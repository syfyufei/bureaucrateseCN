import os
import torch
import numpy as np
import pandas as pd
from pathlib import Path
from transformers import BertModel, BertTokenizer
from tqdm import tqdm
from .download_bert import load_local_bert

def preprocess_official_words(model_name='bert-base-chinese', custom_dict_path=None):
    """预处理官方话语词向量并保存到本地
    
    Args:
        model_name (str): BERT模型名称
        custom_dict_path (str, optional): 自定义词典路径
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # 加载BERT模型
    try:
        package_dir = Path(__file__).parent
        model_dir = package_dir / 'models' / model_name
        tokenizer, model = load_local_bert(model_dir)
        model = model.to(device)
    except FileNotFoundError:
        print(f"本地模型不存在，将从在线下载{model_name}模型...")
        tokenizer = BertTokenizer.from_pretrained(model_name)
        model = BertModel.from_pretrained(model_name).to(device)
    
    model.eval()
    
    # 加载词典
    if custom_dict_path is None:
        package_dir = Path(__file__).parent
        custom_dict_path = package_dir / '../data/RAWdataset.csv'
    
    df = pd.read_csv(custom_dict_path)
    official_words = df[df['typeOfWord'] == '官方话语']['Word'].tolist()
    word_frequencies = dict(zip(df['Word'], df['Frequency']))
    
    # 计算词向量
    official_embeddings = []
    official_weights = []
    
    print("正在计算官方话语词向量...")
    with torch.no_grad():
        for word in tqdm(official_words, desc="处理进度"):
            inputs = tokenizer(word, return_tensors='pt', padding=True)
            inputs = {k: v.to(device) for k, v in inputs.items()}
            outputs = model(**inputs)
            embedding = outputs.last_hidden_state[:, 0, :].cpu().numpy()
            official_embeddings.append(embedding[0])
            official_weights.append(word_frequencies.get(word, 1.0))
    
    official_embeddings = np.array(official_embeddings)
    official_weights = np.array(official_weights)
    official_weights = official_weights / np.sum(official_weights)
    
    # 保存词向量和权重
    save_dir = package_dir / 'preprocessed'
    save_dir.mkdir(exist_ok=True)
    
    np.save(save_dir / 'official_embeddings.npy', official_embeddings)
    np.save(save_dir / 'official_weights.npy', official_weights)
    
    print(f"预处理完成，词向量和权重已保存到 {save_dir}")

if __name__ == '__main__':
    preprocess_official_words()