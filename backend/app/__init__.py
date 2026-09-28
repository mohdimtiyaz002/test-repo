from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import subprocess
import sqlite3
import pickle
import os

app = FastAPI()

# Vulnerability 1: Hardcoded secret
API_KEY = "sk-test-1234567890-super-secret-api-key"

# Vulnerability 2: Hardcoded database credentials
DB_USER = "admin"
DB_PASSWORD = "Admin@123456"
DB_HOST = "10.177.48.25"


@app.get("/")
def home():
    return {
        "application": "AI Security Demo",
        "status": "running"
    }


# Vulnerability 3: Command injection
@app.get("/ping")
def ping(host: str):
    result = subprocess.check_output(
        f"ping -c 1 {host}",
        shell=True
    )

    return {
        "result": result.decode()
    }


# Vulnerability 4: SQL injection
@app.get("/users")
def get_user(username: str):

    conn = sqlite3.connect("users.db")

    query = f"SELECT * FROM users WHERE username = '{username}'"

    cursor = conn.execute(query)

    return {
        "users": cursor.fetchall()
    }


# Vulnerability 5: Unsafe deserialization
@app.post("/load")
async def load_data(request: Request):

    data = await request.body()

    obj = pickle.loads(data)

    return {
        "data": str(obj)
    }


# Vulnerability 6: Information disclosure
@app.get("/debug")
def debug():

    return {
        "environment": dict(os.environ),
        "api_key": API_KEY,
        "database": {
            "host": DB_HOST,
            "username": DB_USER,
            "password": DB_PASSWORD
        }
    }


# Vulnerability 7: Reflected XSS
@app.get("/search")
def search(q: str):

    return HTMLResponse(
        f"<html><body>Search results for: {q}</body></html>"
    )
