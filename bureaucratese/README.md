# Bureaucratese Analyzer | 官方话语分析器

[English](#bureaucratese-analyzer) | [中文](#官方话语分析器)

# Bureaucratese Analyzer

This Python package is specifically designed for quantitative analysis of bureaucratic discourse density in textual content. Through multiple analytical methodologies including fundamental frequency analysis, weighted analysis, and BERT-based semantic analysis, it assists researchers and analysts in measuring and evaluating the prevalence of bureaucratic language in texts.

## Recommended Usage: Web API (New!)

The most recommended way to use this package is through our Web API service. This provides:
- Easy access without complex setup
- Scalable processing for multiple users
- Quota management and monitoring
- Simple HTTP requests from any programming language

### How to Get API Access

To obtain an API key, please send an email to:
**sunyf20@mails.tsinghua.edu.cn**

Include the following information in your email:
- Your name and organization
- Intended use of the API
- Requested quota (number of API calls)

We will process your request and provide you with an API key as soon as possible.

### API Endpoints

Once you have received your API key, you can access the service through these endpoints:

#### 1. Analyze Text
- **URL**: `/analyze`
- **Method**: POST
- **Headers**: 
  - `X-API-Key`: API key
- **Parameters**: 
  - `text`: Text to analyze
  - `method`: Analysis method ("basic", "weighted", "bert", default is "basic")
- **Returns**: Analysis results and remaining quota

#### 2. Batch Analyze Texts
- **URL**: `/analyze/batch`
- **Method**: POST
- **Headers**: 
  - `X-API-Key`: API key
- **JSON Parameters**: 
  - List of texts to analyze
  - `method`: Analysis method ("basic", "weighted", "bert", default is "basic")
- **Returns**: Batch analysis results and remaining quota

#### 3. Query Quota
- **URL**: `/quota`
- **Method**: GET
- **Headers**: 
  - `X-API-Key`: API key
- **Returns**: Quota information

### API Client Example

```python
import requests

# API service address
API_URL = "https://server.drhuyue.site"

# Your API key (obtained via email)
api_key = "your-api-key-here"

# Analyze text
headers = {"X-API-Key": api_key}
text = "深入贯彻新发展理念，全面推进乡村振兴战略，我真的很想吃便宜的水果"
response = requests.post(
    f"{API_URL}/analyze", 
    params={"text": text, "method": "basic"},
    headers=headers
)
result = response.json()
print(result)
```

## Alternative: Direct Package Usage (Not Recommended)

While direct package usage is still supported, it is not recommended for production environments or multi-user scenarios. The following methods are provided for development and testing purposes only.

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

## Quick Start

1. Install the package:
```bash
pip install bureaucratese
```

2. Download BERT model (Optional, required only for semantic analysis):
```python
from bureaucratese.download_bert import download_bert_model
download_bert_model()
```

3. Initialize analysis:
```python
from bureaucratese import BureaucrateseAnalyzer

# Initialize analyzer
analyzer = BureaucrateseAnalyzer()

# Analyze text
text = "深入贯彻新发展理念，全面推进乡村振兴战略，我真的很想吃便宜的水果"
result = analyzer.analyze_text(text)
print(result)
```

[View full English documentation](#functionality)

---

# 官方话语分析器

这是一个专门用于分析文本中官方话语密度的Python包。通过多种分析方法，包括基础频率分析、加权分析和基于BERT的语义分析，帮助研究人员和分析师测量和评估文本中官方话语的使用程度。

## 推荐使用方式：Web API（新！）

使用本包的最推荐方式是通过我们的Web API服务。这提供了：
- 无需复杂设置即可轻松访问
- 为多用户提供可扩展处理
- 配额管理和监控
- 从任何编程语言发送简单的HTTP请求

### 如何获取API访问权限

要获取API密钥，请发送电子邮件至：
**sunyf20@mails.tsinghua.edu.cn**

请在邮件中包含以下信息：
- 您的姓名和组织
- API的预期用途
- 请求的配额（API调用次数）

我们将尽快处理您的请求并提供API密钥。

### API端点

获得API密钥后，您可以通过以下端点访问服务：

#### 1. 分析文本
- **URL**: `/analyze`
- **方法**: POST
- **头部**: 
  - `X-API-Key`: API密钥
- **参数**: 
  - `text`: 要分析的文本
  - `method`: 分析方法（"basic", "weighted", "bert"，默认为"basic"）
- **返回**: 分析结果和剩余配额

#### 2. 批量分析文本
- **URL**: `/analyze/batch`
- **方法**: POST
- **头部**: 
  - `X-API-Key`: API密钥
- **JSON参数**: 
  - 要分析的文本列表
  - `method`: 分析方法（"basic", "weighted", "bert"，默认为"basic"）
- **返回**: 批量分析结果和剩余配额

#### 3. 查询配额
- **URL**: `/quota`
- **方法**: GET
- **头部**: 
  - `X-API-Key`: API密钥
- **返回**: 配额信息

### API客户端示例

```python
import requests

# API服务地址
API_URL = "https://server.drhuyue.site"

# API密钥（通过邮件申请）
api_key = "your-api-key-here"

# 分析文本
headers = {"X-API-Key": api_key}
text = "深入贯彻新发展理念，全面推进乡村振兴战略，我真的很想吃便宜的水果"
response = requests.post(
    f"{API_URL}/analyze", 
    params={"text": text, "method": "basic"},
    headers=headers
)
result = response.json()
print(result)
```

## 替代方式：直接使用包（不推荐）

虽然仍然支持直接使用包，但不建议在生产环境或多用户场景中使用。以下方法仅提供用于开发和测试目的。

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

## 快速开始

1. 安装包：
```bash
pip install bureaucratese
```

2. 下载BERT模型（可选，仅语义分析需要）：
```python
from bureaucratese.download_bert import download_bert_model
download_bert_model()
```

3. 初始化分析：
```python
from bureaucratese import BureaucrateseAnalyzer

# 初始化分析器
analyzer = BureaucrateseAnalyzer()

# 分析文本
text = "深入贯彻新发展理念，全面推进乡村振兴战略，我真的很想吃便宜的水果"
result = analyzer.analyze_text(text)
print(result)
```

## 功能说明

### 基础分析
```python
from bureaucratese import BureaucrateseAnalyzer

# 初始化分析器实例
analyzer = BureaucrateseAnalyzer()

# 分析文本
text = "深入贯彻新发展理念，全面推进乡村振兴战略，我真的很想吃便宜的水果"
result = analyzer.analyze_text(text)
print(result)
```

### 加权分析
```python
# 使用加权分析模式
result = analyzer.analyze_text_weighted(text)
print(result)
```

### 语义分析
```python
# 初始化启用BERT的分析器实例
analyzer = BureaucrateseAnalyzer(use_bert=True)

# 使用BERT分析模式
result = analyzer.analyze_text_with_options(text, mode='bert')
print(result)
```

### 批量分析
```python
# 分析CSV数据集
results = analyzer.analyze_file('data.csv', text_column='content')

# 分析目录内容
results = analyzer.analyze_directory('data_folder/', text_column='content')
```

### 自定义词典

自定义词典必须为CSV格式，包含以下列：

- Word：词条
- typeOfWord：分类（official/daily）
- Frequency：使用频率权重（1-100）

示例：
```csv
Word,typeOfWord,Frequency
深入贯彻,official,85
全面推进,official,80
吃饭,daily,95
上班,daily,90
```

实现自定义词典：
```python
analyzer = BureaucrateseAnalyzer(custom_dict_path='custom_dictionary.csv')
```

### 输出选项
```python
# 获取简化输出
result = analyzer.analyze_text_with_options(
    text,
    mode='weighted',
    output_type='simple'
)

# 获取完整分析数据
result = analyzer.analyze_text_with_options(
    text,
    mode='weighted',
    output_type='full'
)
```

## 输出规范

分析输出包含以下指标：

- **density**：基础密度指标（范围：0-1）
- **weighted_density**：加权密度指标（范围：0-1）
- **semantic_density**：BERT语义密度指标（范围：0-1）
- **official_words**：识别出的官方话语词条
- **total_words**：文本总词数
- **official_word_count**：官方话语词数

## 实现示例

以下展示了官方话语和日常用语的对比分析：

```python
from bureaucratese import BureaucrateseAnalyzer

# 初始化启用BERT的分析器
analyzer = BureaucrateseAnalyzer(use_bert=True)

# 示例1：官方话语文本
official_text = """
坚持以习近平新时代中国特色社会主义思想为指导，全面贯彻党的二十大精神，
弘扬伟大建党精神，坚持稳中求进工作总基调，完整准确全面贯彻新发展理念，
加快构建新发展格局，着力推动高质量发展，更好统筹发展和安全。
"""

# 示例2：日常用语文本
daily_text = """
今天下班后去超市买了些水果和蔬菜，准备周末在家做顿好吃的。
路上碰到了老王，聊了会儿孩子上学的事情，他家孩子今年考上了重点中学，
他们全家都特别高兴。
"""

# 分析官方话语文本
official_result = analyzer.analyze_text_with_options(official_text, mode='bert')
print("官方话语文本分析结果：")
print(f"密度：{official_result['density']:.2%}")
print(f"语义密度：{official_result['semantic_density']:.2%}")
print(f"识别出的官方话语词条：{', '.join(official_result['official_words'])}")

# 分析日常用语文本
daily_result = analyzer.analyze_text_with_options(daily_text, mode='bert')
print("\n日常用语文本分析结果：")
print(f"密度：{daily_result['density']:.2%}")
print(f"语义密度：{daily_result['semantic_density']:.2%}")
print(f"识别出的官方话语词条：{', '.join(daily_result['official_words'])}")
```

## 重要说明

1. BERT模型初始化需要下载功能，请确保网络连接
2. 对于大规模文本分析，请使用批量处理功能
3. 自定义词典文件必须符合指定格式（CSV格式，包含Word、typeOfWord、Frequency列）
4. 使用BERT分析时，根据需求调整batch_size参数

## Web API使用指南

### API端点

- **基础URL**：`https://server.drhuyue.site/v1`

#### 文本分析端点

```
POST /analyze
```

**请求参数：**

```json
{
    "text": "待分析的文本内容",
    "mode": "bert",  // 可选: basic, weighted, bert
    "output_type": "full"  // 可选: simple, full
}
```

**响应格式：**

```json
{
    "status": "success",
    "data": {
        "density": 0.45,
        "weighted_density": 0.38,
        "semantic_density": 0.62,
        "official_words": ["深入贯彻", "全面推进"],
        "total_words": 25,
        "official_word_count": 8
    }
}
```

### API使用示例

#### Python

```python
import requests

# API配置
API_URL = "https://server.drhuyue.site/v1/analyze"

# 准备请求数据
data = {
    "text": "深入贯彻新发展理念，全面推进乡村振兴战略",
    "mode": "bert",
    "output_type": "full"
}

# 发送请求
response = requests.post(API_URL, json=data)

# 处理响应
if response.status_code == 200:
    result = response.json()
    print(f"分析结果：\n{result}")
else:
    print(f"请求失败：{response.status_code}")
```

#### cURL

```bash
curl -X POST "https://server.drhuyue.site/v1/analyze" \
     -H "Content-Type: application/json" \
     -d '{
         "text": "深入贯彻新发展理念，全面推进乡村振兴战略",
         "mode": "bert",
         "output_type": "full"
     }'
```

#### JavaScript

```javascript
const analyzeText = async () => {
    const API_URL = 'https://server.drhuyue.site/v1/analyze';
    
    const data = {
        text: "深入贯彻新发展理念，全面推进乡村振兴战略",
        mode: "bert",
        output_type: "full"
    };
    
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        console.log('分析结果：', result);
    } catch (error) {
        console.error('请求失败：', error);
    }
};

// 调用函数
analyzeText();
```

### 错误处理

错误响应格式：

```json
{
    "status": "error",
    "error": {
        "code": "INVALID_INPUT",
        "message": "文本内容不能为空"
    }
}
```

常见错误代码：

- `INVALID_INPUT`: 输入参数无效
- `TEXT_TOO_LONG`: 文本超出长度限制
- `INVALID_MODE`: 分析模式参数无效
- `SERVER_ERROR`: 服务器内部错误

### 性能优化

1. **批量分析**
   - 使用批量API端点 `/analyze/batch` 处理多个文本
   - 单次请求最多支持100个文本

2. **并发请求**
   - 建议使用连接池管理并发请求
   - 推荐并发数：5-10

3. **缓存策略**
   - 对重复文本的分析结果进行缓存
   - 缓存有效期：24小时

## 开源协议

MIT License

## 贡献指南

欢迎通过GitHub Issues或Pull Requests提供改进和贡献。

1. Fork此仓库
2. 创建特性分支（git checkout -b feature/AmazingFeature）
3. 提交更改（git commit -m 'Add some AmazingFeature'）
4. 推送到分支（git push origin feature/AmazingFeature）
5. 创