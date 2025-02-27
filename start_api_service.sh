#!/bin/bash

# 激活虚拟环境
source /opt/bureaucratese/venv/bin/activate

# 启动API服务
cd /opt/bureaucratese
nohup gunicorn bureaucratese.web_api:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 > api_service.log 2>&1 &

echo "API服务已在后台启动，端口8000，日志文件：api_service.log"
echo "您可以使用 'curl http://localhost:8000/docs' 来检查服务是否正常运行"
