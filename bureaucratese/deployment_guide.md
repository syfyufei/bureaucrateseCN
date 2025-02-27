# Bureaucratese API 部署指南

本指南将帮助你在Ubuntu服务器上部署Bureaucratese API服务。

## 1. 环境配置

### 1.1 安装系统依赖
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nginx sqlite3
```

### 1.2 创建项目目录
```bash
mkdir -p /opt/bureaucratese
cd /opt/bureaucratese
```

### 1.3 创建虚拟环境
```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. 项目部署

### 2.1 上传项目文件
将项目文件上传到服务器：
```bash
# 在本地执行
scp -r ./* user@your-server:/opt/bureaucratese/
```

### 2.2 安装依赖
```bash
pip install -r requirements.txt
pip install gunicorn
```

### 2.3 下载BERT模型
```bash
python -m bureaucratese.download_bert
```

## 3. 配置Gunicorn

### 3.1 创建Gunicorn服务配置
创建文件 `/etc/systemd/system/bureaucratese.service`：

```ini
[Unit]
Description=Bureaucratese API
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/opt/bureaucratese
Environment="PATH=/opt/bureaucratese/venv/bin"
ExecStart=/opt/bureaucratese/venv/bin/gunicorn bureaucratese.web_api:app -w 4 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:8000

[Install]
WantedBy=multi-user.target
```

### 3.2 启动服务
```bash
sudo systemctl start bureaucratese
sudo systemctl enable bureaucratese
```

## 4. 配置Nginx

### 4.1 创建Nginx配置
创建文件 `/etc/nginx/sites-available/bureaucratese`：

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 4.2 启用站点
```bash
sudo ln -s /etc/nginx/sites-available/bureaucratese /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 5. SSL配置（可选但推荐）

### 5.1 安装Certbot
```bash
sudo apt install -y certbot python3-certbot-nginx
```

### 5.2 获取SSL证书
```bash
sudo certbot --nginx -d your-domain.com
```

## 6. 防火墙配置

```bash
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

## 7. 测试部署

### 7.1 注册新用户
```bash
curl -X POST "https://your-domain.com/register?quota=1000"
```

### 7.2 测试API
```bash
curl -X POST "https://your-domain.com/analyze" \
     -H "X-API-Key: your-api-key" \
     -H "Content-Type: application/json" \
     -d '{"text": "深入贯彻落实科学发展观"}'
```

## 8. 维护说明

### 8.1 查看日志
```bash
sudo journalctl -u bureaucratese.service
```

### 8.2 重启服务
```bash
sudo systemctl restart bureaucratese
```

### 8.3 更新代码
```bash
cd /opt/bureaucratese
source venv/bin/activate
git pull  # 如果使用git管理
pip install -r requirements.txt  # 如果依赖有更新
sudo systemctl restart bureaucratese
```

## 注意事项

1. 请确保服务器有足够的内存运行BERT模型（建议至少4GB RAM）
2. 定期备份SQLite数据库文件
3. 监控服务器资源使用情况
4. 根据需要调整Gunicorn的工作进程数
5. 考虑设置API请求速率限制