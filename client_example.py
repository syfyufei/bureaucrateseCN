#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

# API服务地址
API_URL = "http://localhost:8000"

# 示例API密钥（请替换为您的API密钥）
API_KEY = "your_api_key_here"

def analyze_text(text, api_key, method="basic"):
    """分析文本的官方话语密度"""
    headers = {"X-API-Key": api_key}
    response = requests.post(
        f"{API_URL}/analyze", 
        params={"text": text, "method": method},
        headers=headers
    )
    return response.json()

def analyze_batch(texts, api_key, method="basic"):
    """批量分析文本的官方话语密度"""
    headers = {"X-API-Key": api_key}
    response = requests.post(
        f"{API_URL}/analyze/batch", 
        json={"texts": texts, "method": method},
        headers=headers
    )
    return response.json()

def get_quota(api_key):
    """查询剩余API调用次数"""
    headers = {"X-API-Key": api_key}
    response = requests.get(f"{API_URL}/quota", headers=headers)
    return response.json()

if __name__ == "__main__":
    print("官方话语分析API客户端示例")
    print("注意：请先替换代码中的API_KEY为您的实际API密钥")
    print("API服务地址：", API_URL)
    print()
    
    # 查询配额信息
    try:
        quota_info = get_quota(API_KEY)
        print("配额信息:")
        print(json.dumps(quota_info, ensure_ascii=False, indent=2))
        print()
    except Exception as e:
        print(f"获取配额失败: {e}")
        print("请确保您已替换API_KEY并且API服务正在运行")
        exit(1)
    
    # 分析单个文本
    text = "坚持以习近平新时代中国特色社会主义思想为指导，全面贯彻党的二十大精神"
    print(f"分析文本: {text}")
    
    # 使用基础分析方法
    try:
        basic_result = analyze_text(text, API_KEY, method="basic")
        print("基础分析结果:")
        print(json.dumps(basic_result, ensure_ascii=False, indent=2))
        print()
    except Exception as e:
        print(f"基础分析失败: {e}")
    
    # 使用加权分析方法
    try:
        weighted_result = analyze_text(text, API_KEY, method="weighted")
        print("加权分析结果:")
        print(json.dumps(weighted_result, ensure_ascii=False, indent=2))
        print()
    except Exception as e:
        print(f"加权分析失败: {e}")
    
    # 使用BERT分析方法
    try:
        bert_result = analyze_text(text, API_KEY, method="bert")
        print("BERT分析结果:")
        print(json.dumps(bert_result, ensure_ascii=False, indent=2))
        print()
    except Exception as e:
        print(f"BERT分析失败: {e}")
    
    # 批量分析示例
    texts = [
        "坚持以习近平新时代中国特色社会主义思想为指导",
        "全面贯彻党的二十大精神",
        "这是一个普通的句子，没有官方话语"
    ]
    print(f"批量分析 {len(texts)} 个文本:")
    
    try:
        batch_result = analyze_batch(texts, API_KEY, method="basic")
        print("批量分析结果:")
        print(json.dumps(batch_result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"批量分析失败: {e}")
