# Bureaucratese API 服务设置摘要

## 服务配置

- **服务地址**: https://server.drhuyue.site
- **管理员密钥**: `bureaucratese_admin_2025`
- **联系邮箱**: sunyf20@mails.tsinghua.edu.cn

## 文件结构

- `/opt/bureaucratese/` - 主目录
  - `bureaucratese/` - 核心包目录
    - `web_api.py` - FastAPI Web服务实现
    - `analyzer.py` - 文本分析实现
    - `models/` - BERT模型目录
  - `start_api_service.sh` - 启动API服务脚本
  - `stop_api_service.sh` - 停止API服务脚本
  - `client_example.py` - API客户端示例
  - `admin_tools.py` - 管理员工具脚本
  - `requirements.txt` - Python依赖包列表
  - `README.md` - 项目说明文档
  - `ADMIN_GUIDE.md` - 管理员指南
  - `download_bert_model.py` - BERT模型下载脚本
  - `api_service.log` - API服务日志文件

## 安装步骤

1. 解压项目文件到 `/opt/bureaucratese/`
2. 创建并激活Python虚拟环境
3. 安装依赖: `pip install -r requirements.txt`
4. 下载BERT模型: `python download_bert_model.py`
5. 启动服务: `./start_api_service.sh`

## API访问控制

- 移除了公开的`/register`端点
- 添加了`/admin/create_user`端点，需要管理员密钥
- 用户需通过电子邮件申请API密钥
- 管理员使用`admin_tools.py`创建用户并分配API密钥

## 用户管理流程

1. 用户通过电子邮件请求API访问权限
2. 管理员评估请求并决定配额
3. 管理员使用管理员工具创建用户
4. 管理员将API密钥发送给用户

## 服务管理

- 启动服务: `./start_api_service.sh`
- 停止服务: `./stop_api_service.sh`
- 服务日志: `api_service.log`

## 安全注意事项

- 管理员密钥应妥善保管
- API密钥通过安全渠道传输给用户
- 定期检查日志文件，监控异常活动
- 使用HTTPS加密通信，保护API密钥和数据传输安全
