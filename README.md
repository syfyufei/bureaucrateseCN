# Bureaucratese Analyzer | “官腔”分析器

[![PyPI version](https://img.shields.io/pypi/v/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![PyPI downloads](https://img.shields.io/pypi/dm/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![Python versions](https://img.shields.io/pypi/pyversions/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![License](https://img.shields.io/github/license/adrian/bureaucratese.svg)](https://github.com/adrian/bureaucratese/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[English](#bureaucratese-analyzer) | [中文](#chinese)

---

<a name="english"></a>
# Bureaucratese Analyzer

This Python package is specifically designed for quantitative analysis of bureaucratic discourse density in textual content. Through multiple analytical methodologies including fundamental frequency analysis, weighted analysis, and BERT-based semantic analysis, it assists researchers and analysts in measuring and evaluating the prevalence of bureaucratic language in texts.

## Installation

```bash
pip install bureaucratese
```

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

# Analyze with BERT semantic method
response = requests.post(f"{API_URL}/analyze", params={"text": text, "method": "bert"})
result = response.json()
print(f"BERT analysis result: {result}")
```

## Alternative: Direct Package Usage

If you prefer to use the package directly in your Python code, you can install it and use it as follows:

```python
from bureaucratese import BureaucrateseAnalyzer

# Initialize analyzer
analyzer = BureaucrateseAnalyzer()

# Analyze text with basic method
text = "深入贯彻新发展理念，全面推进乡村振兴战略"
result = analyzer.analyze_text(text)
print(f"Basic analysis result: {result}")

# Analyze with weighted method
result = analyzer.analyze_text_weighted(text)
print(f"Weighted analysis result: {result}")

# Initialize with BERT support
analyzer_bert = BureaucrateseAnalyzer(use_bert=True)

# Analyze with BERT semantic method
result = analyzer_bert.analyze_text_with_options(text, mode='bert')
print(f"BERT analysis result: {result}")
```

## Analysis Methods

### Basic Density Analysis

The basic density is calculated as:

```
Density = Number of bureaucratic terms / Total number of words
```

This provides a straightforward measure of how much of the text consists of bureaucratic language.

### Weighted Density Analysis

The weighted density incorporates the frequency and importance of different bureaucratic terms:

```
Weighted Density = Sum(Term Weight × Term Occurrence) / Total number of words
```

This method assigns different weights to bureaucratic terms based on their frequency in official documents. Terms that appear more frequently in bureaucratic contexts receive higher weights, providing a more nuanced analysis.

### BERT Semantic Analysis

The BERT semantic analysis uses contextual embeddings to identify bureaucratic language patterns:

```
Semantic Density = Semantic similarity to bureaucratic reference corpus
```

This advanced method can identify bureaucratic language even when specific terms are not in our dictionary, by analyzing the semantic similarity to known bureaucratic texts.

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
- Initial release on PyPI
- Basic, weighted, and BERT-based analysis
- Web API support

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<a name="chinese"></a>
# 官腔分析器

[![PyPI version](https://img.shields.io/pypi/v/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![PyPI downloads](https://img.shields.io/pypi/dm/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![Python versions](https://img.shields.io/pypi/pyversions/bureaucratese.svg)](https://pypi.org/project/bureaucratese/)
[![License](https://img.shields.io/github/license/adrian/bureaucratese.svg)](https://github.com/adrian/bureaucratese/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

这是一个专门用于分析文本中官方话语密度的Python包。通过多种分析方法，包括基础频率分析、加权分析和基于BERT的语义分析，帮助研究人员和分析师测量和评估文本中官方话语的使用程度。

## 安装

```bash
pip install bureaucratese
```

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

我们强烈建议使用我们的Web API进行所有分析需求。API相比本地安装提供了几个优势：

1. **无需设置**：避免复杂的安装和依赖管理
2. **始终更新**：访问最新的分析算法和词典
3. **可扩展性能**：高效处理大量文本
4. **跨平台兼容性**：可从任何编程语言或环境使用

### API使用入门

```python
import requests

# API地址
API_URL = "http://server.drhuyue.site:8000"

# 使用基本方法分析文本
text = "深入贯彻新发展理念，全面推进乡村振兴战略"
response = requests.post(f"{API_URL}/analyze", params={"text": text, "method": "basic"})
result = response.json()
print(f"基本分析结果: {result}")

# 使用加权方法分析
response = requests.post(f"{API_URL}/analyze", params={"text": text, "method": "weighted"})
result = response.json()
print(f"加权分析结果: {result}")

# 使用BERT语义方法分析
response = requests.post(f"{API_URL}/analyze", params={"text": text, "method": "bert"})
result = response.json()
print(f"BERT分析结果: {result}")
```

## 替代方案：直接使用包

如果您更喜欢在Python代码中直接使用该包，可以按照以下方式安装和使用：

```python
from bureaucratese import BureaucrateseAnalyzer

# 初始化分析器
analyzer = BureaucrateseAnalyzer()

# 使用基本方法分析文本
text = "深入贯彻新发展理念，全面推进乡村振兴战略"
result = analyzer.analyze_text(text)
print(f"基本分析结果: {result}")

# 使用加权方法分析
result = analyzer.analyze_text_weighted(text)
print(f"加权分析结果: {result}")

# 初始化支持BERT的分析器
analyzer_bert = BureaucrateseAnalyzer(use_bert=True)

# 使用BERT语义方法分析
result = analyzer_bert.analyze_text_with_options(text, mode='bert')
print(f"BERT分析结果: {result}")
```

## 分析方法

### 基本密度分析

基本密度计算公式为：

```
密度 = 官方话语术语数量 / 总词数
```

这提供了一个直观的衡量标准，表示文本中有多少部分是官方话语。

### 加权密度分析

加权密度分析考虑了不同官方话语术语的频率和重要性：

```
加权密度 = 总和(术语权重 × 术语出现次数) / 总词数
```

此方法根据官方文件中的频率为不同的官方话语术语分配不同的权重。在官方语境中出现频率更高的术语获得更高的权重，提供更细致的分析。

### BERT语义分析

BERT语义分析使用上下文嵌入来识别官方话语模式：

```
语义密度 = 与官方话语参考语料库的语义相似度
```

这种高级方法可以识别官方话语，即使特定术语不在我们的词典中，通过分析与已知官方文本的语义相似性。

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
- 在PyPI上的初始发布
- 基础、加权和基于BERT的分析
- Web API支持

## 许可证

本项目采用MIT许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。
