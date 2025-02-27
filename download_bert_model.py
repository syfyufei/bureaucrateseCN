from transformers import BertModel, BertTokenizer
import os

# 创建模型目录
os.makedirs("models/bert-base-chinese", exist_ok=True)

print("正在下载BERT模型...")
# 下载模型和分词器
tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
model = BertModel.from_pretrained("bert-base-chinese")

# 保存模型和分词器
print("正在保存模型到本地...")
tokenizer.save_pretrained("models/bert-base-chinese")
model.save_pretrained("models/bert-base-chinese")

print("BERT模型下载完成！")
