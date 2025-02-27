from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import APIKeyHeader
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import jwt
import sqlite3
import uuid
from .api import BureaucrateseAPI

app = FastAPI(
    title="Bureaucratese API",
    description="官方话语分析API服务",
    version="1.0.0"
)

# 数据库初始化
def init_db():
    conn = sqlite3.connect('bureaucratese.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            api_key TEXT UNIQUE,
            quota INTEGER,
            used_count INTEGER DEFAULT 0,
            created_at TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# 初始化数据库
init_db()

# API密钥认证
api_key_header = APIKeyHeader(name="X-API-Key")

# 用户认证中间件
def get_current_user(api_key: str = Depends(api_key_header)):
    conn = sqlite3.connect('bureaucratese.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE api_key = ?', (api_key,))
    user = c.fetchone()
    conn.close()
    
    if not user:
        raise HTTPException(status_code=401, detail="无效的API密钥")
    
    if user[2] <= user[3]:  # quota <= used_count
        raise HTTPException(status_code=403, detail="API调用次数已达上限")
    
    return {"id": user[0], "api_key": user[1], "quota": user[2], "used_count": user[3]}

# 初始化分析器
analyzer = BureaucrateseAPI(use_bert=True)

# 管理员密钥 - 在实际应用中应该存储在安全的环境变量或配置文件中
ADMIN_KEY = "bureaucratese_admin_2025"

@app.post("/admin/create_user")
def create_user(quota: int = 1000, admin_key: str = Header(None)):
    """管理员创建新用户并生成API密钥"""
    if admin_key != ADMIN_KEY:
        raise HTTPException(status_code=403, detail="管理员密钥无效")
        
    user_id = str(uuid.uuid4())
    api_key = str(uuid.uuid4())
    
    conn = sqlite3.connect('bureaucratese.db')
    c = conn.cursor()
    c.execute(
        'INSERT INTO users (id, api_key, quota, created_at) VALUES (?, ?, ?, ?)',
        (user_id, api_key, quota, datetime.now())
    )
    conn.commit()
    conn.close()
    
    return {"user_id": user_id, "api_key": api_key, "quota": quota}

@app.post("/analyze")
def analyze_text(text: str, method: str = "basic", user: dict = Depends(get_current_user)):
    """分析文本的官方话语密度"""
    # 更新使用次数
    conn = sqlite3.connect('bureaucratese.db')
    c = conn.cursor()
    c.execute('UPDATE users SET used_count = used_count + 1 WHERE api_key = ?', (user["api_key"],))
    conn.commit()
    conn.close()
    
    try:
        result = analyzer.analyze_text(text, method)
        return {
            "result": result,
            "remaining_quota": user["quota"] - (user["used_count"] + 1)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/analyze/batch")
def analyze_texts(texts: List[str], method: str = "basic", user: dict = Depends(get_current_user)):
    """批量分析多个文本的官方话语密度"""
    # 更新使用次数（每个文本计数一次）
    conn = sqlite3.connect('bureaucratese.db')
    c = conn.cursor()
    c.execute(
        'UPDATE users SET used_count = used_count + ? WHERE api_key = ?',
        (len(texts), user["api_key"])
    )
    conn.commit()
    conn.close()
    
    try:
        results = analyzer.analyze_texts(texts, method)
        return {
            "results": results,
            "remaining_quota": user["quota"] - (user["used_count"] + len(texts))
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/quota")
def get_quota(user: dict = Depends(get_current_user)):
    """查询剩余API调用次数"""
    return {
        "quota": user["quota"],
        "used_count": user["used_count"],
        "remaining_quota": user["quota"] - user["used_count"]
    }