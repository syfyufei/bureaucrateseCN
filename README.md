# Bureaucratese / 官方话语分析工具

[English](#english) | [中文](#chinese)

---

<a name="english"></a>
# Bureaucratese Analysis Tool

A Python tool for analyzing bureaucratic discourse density in text.

## Introduction

Bureaucratese Analysis Tool is a Python package designed to analyze the density of bureaucratic discourse in texts. This tool can help researchers, journalists, and the public analyze the use of official language in government documents, news reports, and other texts.

## Features

- Basic bureaucratic discourse density analysis
- Weighted bureaucratic discourse density analysis
- BERT-based semantic analysis
- Python API interface
- Web API service
- Batch text analysis

## Installation

```bash
# Clone the repository
git clone https://github.com/syfyufei/bureaucratese.git
cd bureaucratese

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .

# Download BERT model (if you need to use BERT analysis)
python download_bert_model.py
```

## Usage

### Python API

```python
from bureaucratese import Analyzer

# Create an analyzer instance
analyzer = Analyzer()

# Analyze text
text = "坚持以习近平新时代中国特色社会主义思想为指导，全面贯彻党的二十大精神"
result = analyzer.analyze(text)
print(f"Bureaucratic discourse density: {result['density']}")
print(f"Bureaucratic terms: {result['official_words']}")

# Use weighted analysis
weighted_result = analyzer.analyze(text, method="weighted")
print(f"Weighted bureaucratic discourse density: {weighted_result['weighted_density']}")

# Use BERT analysis (requires downloading the BERT model first)
bert_result = analyzer.analyze(text, method="bert")
print(f"BERT analysis bureaucratic discourse density: {bert_result['density']}")
```

### Web API

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
API_URL = "http://localhost:8000"

# Analyze text
text = "坚持以习近平新时代中国特色社会主义思想为指导，全面贯彻党的二十大精神"
response = requests.post(f"{API_URL}/analyze", params={"text": text})
result = response.json()
print(result)
```

## Web API Documentation

After starting the API service, you can access the API documentation at:

- http://localhost:8000/docs

## Examples

See the `examples` directory for more usage examples.

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
# 官方话语分析工具

用于分析文本中官方话语密度的Python工具。

## 简介

官方话语分析工具是一个用于分析文本中官方话语使用密度的Python工具包。该工具可以帮助研究人员、记者和公众分析政府文件、新闻报道和其他文本中官方话语的使用情况。

## 功能特点

- 基础官方话语密度分析
- 加权官方话语密度分析
- 基于BERT的语义分析
- Python API接口
- Web API服务
- 批量文本分析

## 安装方法

```bash
# 克隆仓库
git clone https://github.com/syfyufei/bureaucratese.git
cd bureaucratese

# 安装依赖
pip install -r requirements.txt

# 安装包
pip install -e .

# 下载BERT模型（如果需要使用BERT分析）
python download_bert_model.py
```

## 使用方法

### Python API

```python
from bureaucratese import Analyzer

# 创建分析器实例
analyzer = Analyzer()

# 分析文本
text = "坚持以习近平新时代中国特色社会主义思想为指导，全面贯彻党的二十大精神"
result = analyzer.analyze(text)
print(f"官方话语密度: {result['density']}")
print(f"官方话语词汇: {result['official_words']}")

# 使用加权分析
weighted_result = analyzer.analyze(text, method="weighted")
print(f"加权官方话语密度: {weighted_result['weighted_density']}")

# 使用BERT分析（需要先下载BERT模型）
bert_result = analyzer.analyze(text, method="bert")
print(f"BERT分析官方话语密度: {bert_result['density']}")
```

### Web API

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
API_URL = "http://localhost:8000"

# 分析文本
text = "坚持以习近平新时代中国特色社会主义思想为指导，全面贯彻党的二十大精神"
response = requests.post(f"{API_URL}/analyze", params={"text": text})
result = response.json()
print(result)
```

## Web API文档

API服务启动后，可以访问以下地址查看API文档：

- http://localhost:8000/docs

## 示例

查看`examples`目录获取更多使用示例。

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
