from flask import Flask
import json
import os

app = Flask(__name__)

config_path = os.path.join(os.path.dirname(__file__), '../../../agent_configs.json')
with open(config_path, 'r') as f:
    config = json.load(f)

@app.route('/')
def home() -> str:
    return "DevDollz Kernel Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
