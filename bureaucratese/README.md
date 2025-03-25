# Bureaucratese Analyzer | 官方话语分析器

[![PyPI version](https://img.shields.io/pypi/v/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![PyPI downloads](https://img.shields.io/pypi/dm/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![Python versions](https://img.shields.io/pypi/pyversions/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![License](https://img.shields.io/github/license/adrian/bureaucratese.svg)](https://github.com/adrian/bureaucratese/blob/main/LICENSE)
[![Build status](https://img.shields.io/github/workflow/status/adrian/bureaucratese/CI)](https://github.com/adrian/bureaucratese/actions)
[![Documentation Status](https://readthedocs.io/en/latest/?badge=latest)](https://bureaucratese.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[English](#bureaucratese-analyzer) | [中文](#官方话语分析器)

# Bureaucratese Analyzer

This Python package is specifically designed for quantitative analysis of bureaucratic discourse density in textual content. Through multiple analytical methodologies including fundamental frequency analysis, weighted analysis, and BERT-based semantic analysis, it assists researchers and analysts in measuring and evaluating the prevalence of bureaucratic language in texts.

## Installation

```bash
pip install bureaucratese
```

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

## Alternative: Direct Package Usage

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

## Documentation

For full documentation, please visit [bureaucratese.readthedocs.io](https://bureaucratese.readthedocs.io/).

## Development

### Prerequisites

- Python 3.6+
- pip

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/adrian/bureaucratese.git
cd bureaucratese

# Install development dependencies
pip install -e ".[dev]"
```

### Running tests

```bash
pytest
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Changelog

### 0.1.0 (2025-03-25)
- Initial release
- Basic, weighted, and BERT-based analysis
- Web API support

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
# 官方话语分析器

[![PyPI version](https://img.shields.io/pypi/v/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![PyPI downloads](https://img.shields.io/pypi/dm/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![Python versions](https://img.shields.io/pypi/pyversions/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![License](https://img.shields.io/github/license/adrian/bureaucratese.svg)](https://github.com/adrian/bureaucratese/blob/main/LICENSE)
[![Build status](https://img.shields.io/github/workflow/status/adrian/bureaucratese/CI)](https://github.com/adrian/bureaucratese/actions)
[![Documentation Status](https://readthedocs.io/en/latest/?badge=latest)](https://bureaucratese.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

这是一个专门用于分析文本中官方话语密度的Python包。通过多种分析方法，包括基础频率分析、加权分析和基于BERT的语义分析，帮助研究人员和分析师测量和评估文本中官方话语的使用程度。

## 安装

```bash
pip install bureaucratese
```

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

## 替代方式：直接使用包

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

## 文档

完整文档请访问 [bureaucratese.readthedocs.io](https://bureaucratese.readthedocs.io/)。

## 开发

### 先决条件

- Python 3.6+
- pip

### 设置开发环境

```bash
# 克隆仓库
git clone https://github.com/adrian/bureaucratese.git
cd bureaucratese

# 安装开发依赖
pip install -e ".[dev]"
```

### 运行测试

```bash
pytest
```

### 贡献

欢迎贡献！请随时提交Pull Request。

1. Fork仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m '添加一些惊人的特性'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开Pull Request

## 更新日志

### 0.1.0 (2025-03-25)
- 初始发布
- 基础、加权和基于BERT的分析
- Web API支持

## 许可证

本项目采用MIT许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。