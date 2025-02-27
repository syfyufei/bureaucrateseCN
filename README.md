# Bureaucratese Analyzer | “官腔”分析器

[English](#bureaucratese-analyzer) | [中文](#“官腔”分析器)

---

<a name="english"></a>
# Bureaucratese Analyzer

This Python package is specifically designed for quantitative analysis of bureaucratic discourse density in textual content. Through multiple analytical methodologies including fundamental frequency analysis, weighted analysis, and BERT-based semantic analysis, it assists researchers and analysts in measuring and evaluating the prevalence of bureaucratic language in texts.

## Key Features

- **Multi-dimensional Analysis Modes**:
  - Fundamental Density Analysis: Bureaucratic discourse density analysis based on word frequency
  - Weighted Density Analysis: Advanced analysis incorporating word frequency weights
  - BERT Semantic Analysis: Deep semantic similarity analysis utilizing BERT models

- **Flexible Configuration Options**:
  - Custom dictionary integration support
  - Optional BERT model implementation
  - Multiple output format specifications

- **Batch Processing Capabilities**:
  - Single document analysis
  - Directory-level batch processing
  - DataFrame output support

## Recommended: Using the API for Analysis

We strongly recommend using our Web API for all analysis needs. The API provides several advantages over local installation:

1. **No Setup Required**: Avoid complex installation and dependency management
2. **Always Updated**: Access the latest analysis algorithms and dictionaries
3. **Scalable Performance**: Process large volumes of text efficiently
4. **Cross-Platform Compatibility**: Use from any programming language or environment

### Getting Started with the API

```python
import requests

# API address
API_URL = "http://server.drhuyue.site:8000"

# Analyze text with basic method
text = "深入贯彻新发展理念，全面推进乡村振兴战略"
response = requests.post(f"{API_URL}/analyze", params={"text": text, "method": "basic"})
result = response.json()
print(f"Basic analysis result: {result}")

# Analyze with weighted method
response = requests.post(f"{API_URL}/analyze", params={"text": text, "method": "weighted"})
result = response.json()
print(f"Weighted analysis result: {result}")

# Analyze with semantic method
response = requests.post(f"{API_URL}/analyze", params={"text": text, "method": "semantic"})
result = response.json()
print(f"Semantic analysis result: {result}")
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/analyze` | POST | Analyze a single text with specified method |
| `/analyze/batch` | POST | Analyze multiple texts in one request |
| `/quota` | GET | Check your API usage quota |

### API Parameters

| Parameter | Description | Options |
|-----------|-------------|---------|
| `text` | Text to analyze | Any string |
| `method` | Analysis method | `basic`, `weighted`, `semantic` |
| `preprocessing` | Text preprocessing options | `default`, `minimal`, `full` |

## Web API

Start the Web API service:

```bash
# Start the service
./start_api_service.sh

# Or directly with Python
python run_api.py
```

Use the API:

```python
import requests

# API address
API_URL = "http://server.drhuyue.site:8000"

# Analyze text
text = "深入贯彻新发展理念，全面推进乡村振兴战略"
response = requests.post(f"{API_URL}/analyze", params={"text": text, "method": "basic"})
result = response.json()
print(result)
```

## Web API Documentation

After starting the API service, you can access the API documentation at:

- http://server.drhuyue.site:8000/docs

## Output Specifications

Analysis output includes the following metrics:

- **density**: Basic density metric (range: 0-1)
- **weighted_density**: Weighted density metric (range: 0-1)
- **semantic_density**: BERT semantic density metric (range: 0-1)
- **official_words**: Identified bureaucratic terms
- **total_words**: Total word count in the text
- **official_word_count**: Number of bureaucratic words

## Detailed Analysis Methods

### 1. Basic Density Analysis

The basic density analysis calculates the proportion of bureaucratic terms in the text:

```
Density = Number of bureaucratic terms / Total number of words
```

This method provides a straightforward measurement of how prevalent bureaucratic language is in a given text. It identifies specific bureaucratic terms from a predefined dictionary and counts their occurrences.

**Example Output:**
```python
{
    'density': 0.5417,                # 54.17% of words are bureaucratic terms
    'official_words': ['深入', '贯彻', '发展', ...],  # List of identified terms
    'total_words': 24,                # Total word count in the text
    'official_word_count': 13         # Number of bureaucratic terms found
}
```

### 2. Weighted Density Analysis

The weighted density analysis takes into account the frequency or importance of each bureaucratic term:

```
Weighted Density = Sum(Term Weight × Term Occurrence) / Total number of words
```

This method assigns different weights to bureaucratic terms based on their frequency in official documents. Terms that appear more frequently in bureaucratic contexts receive higher weights, providing a more nuanced analysis.

**Example Output:**
```python
{
    'weighted_density': 0.9250,       # Weighted density score
    'official_words': ['深入', '贯彻', '发展', ...],  # List of identified terms
    'total_words': 24,                # Total word count in the text
    'official_word_count': 13         # Number of bureaucratic terms found
}
```

### 3. BERT Semantic Analysis

The BERT semantic analysis uses deep learning to capture semantic similarities between the input text and bureaucratic language patterns:

```
Semantic Density = Cosine similarity between text embedding and bureaucratic term embeddings
```

This advanced method goes beyond simple word matching by using BERT (Bidirectional Encoder Representations from Transformers) to understand the semantic meaning of the text. It can identify bureaucratic language patterns even when specific terms are not present.

**Key features:**
- Captures semantic similarity rather than exact word matches
- Can detect bureaucratic language style and patterns
- Works effectively even with paraphrased bureaucratic expressions

**Example Output:**
```python
{
    'semantic_density': 0.7984,       # Semantic similarity score (0-1)
    'weighted_similarity': 0.5968     # Weighted semantic similarity
}
```

### Comparison of Analysis Methods

| Analysis Method | Strengths | Use Cases |
|-----------------|-----------|-----------|
| Basic Density | Simple, transparent, easy to interpret | Quick analysis, term identification |
| Weighted Density | Considers term importance, more nuanced | Detailed analysis of bureaucratic intensity |
| BERT Semantic | Captures semantic patterns, not just words | Style analysis, detecting subtle bureaucratic language |

For optimal results, we recommend using all three methods to get a comprehensive understanding of bureaucratic language usage in your text.

## Project Structure

```
bureaucratese/
├── bureaucratese/         # Main package directory
│   ├── __init__.py        # Package initialization file
│   ├── analyzer.py        # Core analyzer
│   ├── bert_analyzer.py   # BERT analyzer
│   ├── api.py             # Python API
│   └── web_api.py         # Web API
├── data/                  # Data directory
├── models/                # Model directory
├── examples/              # Example code
├── setup.py               # Installation script
└── README.md              # Documentation
```

## Contact

For any questions, please contact: sunyf20@mails.tsinghua.edu.cn

## License

MIT License

---

<a name="chinese"></a>
# “官腔”分析器

这是一个专门用于分析文本中官方话语密度的Python包。通过多种分析方法，包括基础频率分析、加权分析和基于BERT的语义分析，帮助研究人员和分析师测量和评估文本中官方话语的使用程度。

## 主要特点

- **多维度分析模式**：
  - 基础密度分析：基于词频的官方话语密度分析
  - 加权密度分析：结合词频权重的高级分析
  - BERT语义分析：使用BERT模型的深度语义相似度分析

- **灵活的配置选项**：
  - 支持自定义词典集成
  - 可选的BERT模型实现
  - 多种输出格式规范

- **批量处理能力**：
  - 单文档分析
  - 目录级批量处理
  - DataFrame输出支持

## 推荐：使用API进行分析

我们强烈推荐使用我们的Web API进行所有分析。API提供了以下优势：

1. **无需安装**：避免复杂的安装和依赖管理
2. **始终更新**：访问最新的分析算法和词典
3. **可扩展性能**：高效处理大量文本
4. **跨平台兼容**：从任何编程语言或环境中使用

### API使用示例

```python
import requests
import json

# API服务地址
API_URL = "http://server.drhuyue.site:8000"

# 示例API密钥
API_KEY = "your_api_key_here"  # 请替换为您的API密钥

> **重要提示**：为了使用官腔分析器API服务，您需要获取专属的API密钥。请发送电子邮件至sunyf20@mails.tsinghua.edu.cn申请，邮件主题请注明"申请官腔分析器API密钥"，并简要说明您的使用目的。我们将在收到邮件后尽快回复您，提供专属的API密钥及详细的使用说明。

# 分析单个文本
def analyze_text(text, method="basic"):
    """分析文本的官方话语密度"""
    try:
        headers = {"X-API-Key": API_KEY}
        response = requests.post(
            f"{API_URL}/analyze", 
            params={"text": text, "method": method},
            headers=headers
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        return None

# 批量分析多个文本
def batch_analyze_texts(texts, method="basic"):
    """批量分析多个文本的官方话语密度"""
    try:
        headers = {
            "X-API-Key": API_KEY,
            "Content-Type": "application/json"
        }
        response = requests.post(
            f"{API_URL}/analyze/batch",
            params={"method": method},
            json=texts,
            headers=headers
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"批量分析请求错误: {e}")
        return None

# 查询API使用配额
def get_quota():
    """查询剩余API调用次数"""
    try:
        headers = {"X-API-Key": API_KEY}
        response = requests.get(f"{API_URL}/quota", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"配额查询错误: {e}")
        return None

# 使用示例
# 1. 查询配额
quota_info = get_quota()
print("配额信息:")
print(json.dumps(quota_info, ensure_ascii=False, indent=2))

# 2. 基础分析
text = "深入贯彻习近平新时代中国特色社会主义思想，全面落实党的二十大精神"
result = analyze_text(text, "basic")
print("\n基础分析结果:")
print(json.dumps(result, ensure_ascii=False, indent=2))

# 3. 加权分析
result = analyze_text(text, "weighted")
print("\n加权分析结果:")
print(json.dumps(result, ensure_ascii=False, indent=2))

# 4. 语义分析
result = analyze_text(text, "semantic")
print("\n语义分析结果:")
print(json.dumps(result, ensure_ascii=False, indent=2))

# 5. 批量分析
texts = [
    "坚持以习近平新时代中国特色社会主义思想为指导",
    "全面贯彻党的二十大精神",
    "今天天气真好，我想去公园散步"
]
batch_results = batch_analyze_texts(texts, "basic")
print("\n批量分析结果:")
print(json.dumps(batch_results, ensure_ascii=False, indent=2))
```

### API端点

| 端点 | 方法 | 描述 |
|----------|--------|-------------|
| `/analyze` | POST | 使用指定方法分析单个文本 |
| `/analyze/batch` | POST | 在一个请求中分析多个文本 |
| `/quota` | GET | 检查您的API使用配额 |

### API参数

| 参数 | 描述 | 选项 |
|-----------|-------------|---------|
| `text` | 分析文本 | 任意字符串 |
| `method` | 分析方法 | `basic`, `weighted`, `semantic` |
| `preprocessing` | 文本预处理选项 | `default`, `minimal`, `full` |

### 获取API密钥

要获取API密钥，请发送电子邮件至：sunyf20@mails.tsinghua.edu.cn

邮件主题请注明"申请官腔分析器API密钥"，并简要说明您的使用目的。我们将在收到邮件后尽快回复您，提供专属的API密钥。

每个API密钥都有默认的使用配额限制，如果您需要更高的配额，请在申请邮件中说明您的需求。

## Web API

启动Web API服务：

```bash
# 启动服务
./start_api_service.sh

# 或者直接使用Python
python run_api.py
```

使用API：

```python
import requests

# API地址
API_URL = "http://server.drhuyue.site:8000"

# 分析文本
text = "深入贯彻新发展理念，全面推进乡村振兴战略"
response = requests.post(f"{API_URL}/analyze", params={"text": text, "method": "basic"})
result = response.json()
print(result)
```

## Web API文档

API服务启动后，可以访问以下地址查看API文档：

- http://server.drhuyue.site:8000/docs

## 输出规范

分析输出包含以下指标：

- **density**：基础密度指标（范围：0-1）
- **weighted_density**：加权密度指标（范围：0-1）
- **semantic_density**：BERT语义密度指标（范围：0-1）
- **official_words**：识别出的官方话语词条
- **total_words**：文本总词数
- **official_word_count**：官方话语词数

## 详细分析方法

### 1. 基础密度分析

基础密度分析计算文本中官方话语词汇的比例：

```
密度 = 官方话语词汇数量 / 总词数
```

这种方法直接测量给定文本中官方话语的普遍程度。它从预定义词典中识别特定的官方话语词汇并计算其出现次数。

**示例输出：**
```python
{
    'density': 0.5417,                # 54.17%的词是官方话语
    'official_words': ['深入', '贯彻', '发展', ...],  # 识别出的官方词汇列表
    'total_words': 24,                # 文本中的总词数
    'official_word_count': 13         # 找到的官方话语词汇数量
}
```

### 2. 加权密度分析

加权密度分析考虑了每个官方话语词汇的频率或重要性：

```
加权密度 = Sum(词汇权重 × 词汇出现次数) / 总词数
```

这种方法根据官方文件中的出现频率为官方话语词汇分配不同的权重。在官方语境中出现频率更高的词汇获得更高的权重，提供更细致的分析。

**示例输出：**
```python
{
    'weighted_density': 0.9250,       # 加权密度分数
    'official_words': ['深入', '贯彻', '发展', ...],  # 识别出的官方词汇列表
    'total_words': 24,                # 文本中的总词数
    'official_word_count': 13         # 找到的官方话语词汇数量
}
```

### 3. BERT语义分析

BERT语义分析使用深度学习来捕捉输入文本与官方话语模式之间的语义相似性：

```
语义密度 = 文本嵌入与官方话语词汇嵌入之间的余弦相似度
```

这种高级方法通过使用BERT（Bidirectional Encoder Representations from Transformers）来理解文本的语义含义，超越了简单的词汇匹配。它可以识别官方话语模式，即使特定词汇不存在。

**主要特点：**
- 捕捉语义相似性而非精确词汇匹配
- 可以检测官方话语风格和模式
- 对改写的官方表达方式也能有效工作

**示例输出：**
```python
{
    'semantic_density': 0.7984,       # 语义相似度分数（0-1）
    'weighted_similarity': 0.5968     # 加权语义相似度
}
```

### 分析方法比较

| 分析方法 | 优势 | 使用场景 |
|---------|------|---------|
| 基础密度 | 简单、透明、易于解释 | 快速分析、词汇识别 |
| 加权密度 | 考虑词汇重要性、更细致 | 官方话语强度的详细分析 |
| BERT语义 | 捕捉语义模式，而非仅词汇 | 风格分析、检测微妙的官方语言 |

为获得最佳结果，我们建议同时使用这三种方法，以全面了解文本中官方话语的使用情况。

## 项目结构

```
bureaucratese/
├── bureaucratese/         # 主要包目录
│   ├── __init__.py        # 包初始化文件
│   ├── analyzer.py        # 核心分析器
│   ├── bert_analyzer.py   # BERT分析器
│   ├── api.py             # Python API
│   └── web_api.py         # Web API
├── data/                  # 数据目录
├── models/                # 模型目录
├── examples/              # 示例代码
├── setup.py               # 安装脚本
└── README.md              # 说明文档
```

## 联系方式

如有任何问题，请联系：sunyf20@mails.tsinghua.edu.cn

## 许可证

MIT License
