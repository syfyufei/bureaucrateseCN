from bureaucratese.api import BureaucrateseAPI

# 初始化API
api = BureaucrateseAPI(use_bert=True)

# 示例文本
text = "深入贯彻落实科学发展观，坚持以人为本。"
texts = [
    "深入贯彻落实科学发展观，坚持以人为本。",
    "今天天气很好，我去超市买了一些水果。",
    "要坚持以人民为中心，不断提高人民群众的生活水平。"
]

# 1. 基础密度分析
print("=== 基础密度分析 ===")
result = api.analyze_text(text)
print(f"密度：{result['density']:.2%}")
print(f"检测到的官方话语：{', '.join(result['official_words'])}\n")

# 2. 加权密度分析
print("=== 加权密度分析 ===")
result = api.analyze_text(text, method='weighted')
print(f"加权密度：{result['weighted_density']:.2%}\n")

# 3. BERT语义分析
print("=== BERT语义分析 ===")
result = api.analyze_text(text, method='semantic')
print(f"语义密度：{result['semantic_density']:.2%}\n")

# 4. 批量分析
print("=== 批量分析 ===")
results = api.analyze_texts(texts, method='weighted')
for i, result in enumerate(results, 1):
    print(f"文本{i}加权密度：{result['weighted_density']:.2%}")
print()

# 5. 使用所有方法分析
print("=== 综合分析 ===")
all_results = api.analyze_text_all(text)
print(f"基础密度：{all_results['basic']['density']:.2%}")
print(f"加权密度：{all_results['weighted']['weighted_density']:.2%}")
print(f"语义密度：{all_results['semantic']['semantic_density']:.2%}")