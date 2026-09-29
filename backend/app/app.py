from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Issue: hardcoded secret
API_KEY = "sk-test-123456789-secret"

@app.route("/user")
def get_user():
    username = request.args.get("username")

    # Issue: SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}'"

    conn = sqlite3.connect("users.db")
    result = conn.execute(query).fetchall()

    return str(result)

@app.route("/debug")
def debug():
    # Issue: sensitive information exposure
    return {
        "database": "users.db",
        "api_key": API_KEY,
        "internal_server": "10.10.20.15"
    }

if __name__ == "__main__":
    app.run(debug=True)
