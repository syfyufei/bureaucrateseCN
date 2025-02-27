#!/bin/bash

# 查找并终止gunicorn进程
pkill -f "gunicorn bureaucratese.web_api:app"

echo "API服务已停止"
