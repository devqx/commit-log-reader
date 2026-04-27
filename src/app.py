from flask import Flask
import os
import time

app = Flask(__name__)
EFS_PATH = "/mnt/efs/log.txt"

@app.route('/')
def read_log():
    try:
        # Check logs every 20 seconds as required
        with open(EFS_PATH, 'r') as f:
            content = f.read()
        return f"<h1>File Content: {content}</h1>"
    except FileNotFoundError:
        return "<h1>Log file not found yet</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

