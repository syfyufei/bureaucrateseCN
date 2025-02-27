# 预处理嵌入向量目录

此目录用于存放预处理的官方话语嵌入向量和权重。

## 说明

出于文件大小限制，本公开版本不包含预处理的嵌入向量文件。您需要自行生成这些文件。

## 生成嵌入向量

请使用以下命令生成所需的嵌入向量：

```bash
python -m bureaucratese.preprocess_embeddings
```

该脚本将自动生成以下文件：

- `official_embeddings.npy`: 官方话语词汇的嵌入向量
- `official_weights.npy`: 官方话语词汇的权重

## 文件格式

- `official_embeddings.npy`: NumPy 数组文件，包含词汇的嵌入向量
- `official_weights.npy`: NumPy 数组文件，包含词汇的权重值

## 联系方式

如有任何问题，请联系：sunyf20@mails.tsinghua.edu.cn
