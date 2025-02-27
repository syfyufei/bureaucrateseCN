# 模型目录

此目录用于存放 BERT 模型文件。

## 说明

出于文件大小限制，本公开版本不包含预训练的 BERT 模型文件。您需要自行下载模型文件。

## 获取模型

请使用项目根目录中的 `download_bert_model.py` 脚本下载所需的 BERT 模型：

```bash
python download_bert_model.py
```

该脚本将自动从 Hugging Face 下载 `bert-base-chinese` 模型并放置在正确的位置。

## 模型结构

下载后，此目录应包含以下文件：

- `bert-base-chinese/config.json`
- `bert-base-chinese/model.safetensors`
- `bert-base-chinese/special_tokens_map.json`
- `bert-base-chinese/tokenizer_config.json`
- `bert-base-chinese/vocab.txt`

## 联系方式

如有任何问题，请联系：sunyf20@mails.tsinghua.edu.cn
