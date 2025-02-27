import os
import torch
from transformers import BertModel, BertTokenizer
from tqdm import tqdm
from pathlib import Path

def download_bert_model(model_name='bert-base-chinese', save_dir='models'):
    """下载BERT模型并保存到本地
    
    Args:
        model_name (str): 要下载的BERT模型名称
        save_dir (str): 保存模型的目录
    """
    print(f"开始下载{model_name}模型...")
    
    # 创建保存目录
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    
    # 使用tqdm显示下载进度
    with tqdm(total=2, desc="下载进度") as pbar:
        # 下载tokenizer
        print("\n下载tokenizer...")
        tokenizer = BertTokenizer.from_pretrained(model_name)
        tokenizer.save_pretrained(save_path / model_name)
        pbar.update(1)
        
        # 下载模型
        print("\n下载模型...")
        model = BertModel.from_pretrained(model_name)
        model.save_pretrained(save_path / model_name)
        pbar.update(1)
    
    print(f"\n模型已成功下载并保存到 {save_path / model_name}")

def load_local_bert(model_dir):
    """从本地加载BERT模型
    
    Args:
        model_dir (str): 模型所在目录
    
    Returns:
        tuple: (tokenizer, model)
    """
    model_path = Path(model_dir)
    if not model_path.exists():
        raise FileNotFoundError(f"模型目录 {model_path} 不存在")
    
    print("正在加载本地模型...")
    tokenizer = BertTokenizer.from_pretrained(str(model_path))
    model = BertModel.from_pretrained(str(model_path))
    print("模型加载完成")
    
    return tokenizer, model

if __name__ == '__main__':
    # 设置模型保存路径
    current_dir = Path(__file__).parent
    models_dir = current_dir / 'models'
    
    # 下载并保存模型
    download_bert_model(save_dir=str(models_dir))