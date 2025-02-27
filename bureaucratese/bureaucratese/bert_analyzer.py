import torch
from transformers import BertModel, BertTokenizer
import pandas as pd
import numpy as np
from pathlib import Path
import jieba
import logging
from .download_bert import load_local_bert

# 配置jieba的日志级别
jieba.setLogLevel(logging.INFO)

class BertBureaucrateseAnalyzer:
    def __init__(self, model_name='bert-base-chinese', custom_dict_path=None, use_local_model=True):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # 尝试加载本地模型，如果失败则从在线下载
        if use_local_model:
            try:
                package_dir = Path(__file__).parent
                model_dir = package_dir / 'models' / model_name
                self.tokenizer, self.model = load_local_bert(model_dir)
                self.model = self.model.to(self.device)
            except FileNotFoundError:
                print(f"本地模型不存在，将从在线下载{model_name}模型...")
                self.tokenizer = BertTokenizer.from_pretrained(model_name)
                self.model = BertModel.from_pretrained(model_name).to(self.device)
        else:
            self.tokenizer = BertTokenizer.from_pretrained(model_name)
            self.model = BertModel.from_pretrained(model_name).to(self.device)
        
        self.model.eval()
        
        # 加载词典并初始化词向量
        self._load_dictionary(custom_dict_path)
        self._initialize_word_embeddings()
    
    def _load_dictionary(self, custom_dict_path=None):
        if custom_dict_path is None:
            package_dir = Path(__file__).parent
            custom_dict_path = package_dir / '../data/RAWdataset.csv'
        
        df = pd.read_csv(custom_dict_path)
        self.official_words = df[df['typeOfWord'] == '官方话语']['Word'].tolist()
        self.word_frequencies = dict(zip(df['Word'], df['Frequency']))
    
    def _initialize_word_embeddings(self):
        """初始化官方话语的BERT词向量，优先从预处理文件加载"""
        package_dir = Path(__file__).parent
        preprocessed_dir = package_dir / 'preprocessed'
        embeddings_file = preprocessed_dir / 'official_embeddings.npy'
        weights_file = preprocessed_dir / 'official_weights.npy'
        
        # 尝试从预处理文件加载
        if embeddings_file.exists() and weights_file.exists():
            print("从预处理文件加载词向量和权重...")
            self.official_embeddings = np.load(embeddings_file)
            self.official_weights = np.load(weights_file)
            return
        
        print("预处理文件不存在，重新计算词向量...")
        self.official_embeddings = []
        self.official_weights = []
        
        with torch.no_grad():
            for word in self.official_words:
                inputs = self.tokenizer(word, return_tensors='pt', padding=True)
                inputs = {k: v.to(self.device) for k, v in inputs.items()}
                outputs = self.model(**inputs)
                # 使用[CLS]标记的输出作为词的表示
                embedding = outputs.last_hidden_state[:, 0, :].cpu().numpy()
                self.official_embeddings.append(embedding[0])
                self.official_weights.append(self.word_frequencies.get(word, 1.0))
        
        self.official_embeddings = np.array(self.official_embeddings)
        self.official_weights = np.array(self.official_weights)
        # 归一化权重
        self.official_weights = self.official_weights / np.sum(self.official_weights)
    
    def get_text_embedding(self, text):
        """获取文本的BERT嵌入表示"""
        with torch.no_grad():
            inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            outputs = self.model(**inputs)
            return outputs.last_hidden_state[:, 0, :].cpu().numpy()[0]
    
    def calculate_semantic_density(self, text):
        """计算文本的语义浓度
        
        基于文本的BERT表示与官方话语词向量的加权余弦相似度来计算浓度
        """
        # 确保输入文本是字符串类型
        if not isinstance(text, str) or not text.strip():
            return {
                'semantic_density': 0.0,
                'weighted_similarity': 0.0
            }
        
        # 获取文本的BERT表示
        text_embedding = self.get_text_embedding(text)
        
        # 计算与每个官方话语词向量的余弦相似度
        similarities = []
        for official_embedding in self.official_embeddings:
            similarity = np.dot(text_embedding, official_embedding) / \
                        (np.linalg.norm(text_embedding) * np.linalg.norm(official_embedding))
            similarities.append(similarity)
        
        # 计算加权平均相似度
        similarities = np.array(similarities)
        weighted_similarity = np.sum(similarities * self.official_weights)
        
        # 将相似度映射到[0,1]区间作为浓度值
        semantic_density = (weighted_similarity + 1) / 2
        
        return {
            'semantic_density': semantic_density,
            'weighted_similarity': weighted_similarity
        }