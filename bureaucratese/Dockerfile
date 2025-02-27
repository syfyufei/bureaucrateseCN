# 使用Python 3.9作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDING /app

# 复制项目文件
COPY . /app/

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 下载BERT模型（如果需要）
RUN python -c "from bureaucratese.download_bert import download_bert_model; download_bert_model()"

# 设置环境变量
ENV MODEL_PATH=/app/models/bert-base-chinese
ENV MAX_BATCH_SIZE=32
ENV WORKERS=4

# 暴露API端口
EXPOSE 8000

# 启动服务
CMD ["python", "-m", "uvicorn", "bureaucratese.web_api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]