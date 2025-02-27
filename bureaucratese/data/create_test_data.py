import pandas as pd
import numpy as np

# 创建测试数据
df = pd.DataFrame({
    'date': pd.date_range('2020-01-01', '2023-12-31', periods=400),
    'content_simplified': ['这是一个测试新闻内容，包含一些官方话语如改革开放、社会主义现代化建设、' + str(i) for i in range(400)]
})

# 保存为parquet文件
df.to_parquet('test_news.parquet')
print('测试数据集已创建')