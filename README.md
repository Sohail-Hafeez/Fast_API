# Fast_API
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Learning Repository</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background-color: #eee;
            padding: 2px 5px;
            border-radius: 4px;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        a {
            color: #2980b9;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .section {
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <h1>FastAPI Learning Repository</h1>
    <p>This repository contains my learning projects and experiments with <strong>FastAPI</strong>. It includes tutorials, example APIs, and code samples for building REST APIs using Python.</p>

    <div class="section">
        <h2>📚 Contents</h2>
        <ul>
            <li>Basic FastAPI setup</li>
            <li>Creating endpoints (GET, POST)</li>
            <li>Using request and response models with <code>pydantic</code></li>
            <li>Running FastAPI in local and Colab environments</li>
            <li>Exposing APIs using <code>ngrok</code></li>
            <li>Deploying ML models as APIs</li>
        </ul>
    </div>

    <div class="section">
        <h2>⚙️ Installation</h2>
        <p>To run these projects locally, install the following Python packages:</p>
        <pre>
pip install fastapi uvicorn pydantic flask pyngrok numpy scikit-learn
        </pre>
        <p>Then start the FastAPI server:</p>
        <pre>
uvicorn main:app --reload
        </pre>
    </div>

    <div class="section">
        <h2>🚀 Usage</h2>
        <p>Example API request using <code>requests</code> in Python:</p>
        <pre>
import requests

url = "http://127.0.0.1:8000/predict"
data = {"features": [5.1, 3.5, 1.4, 0.2]}
response = requests.post(url, json=data)
print(response.json())
        </pre>
    </div>

    <div class="section">
        <h2>💡 Notes</h2>
        <ul>
            <li>Colab sessions are temporary; your API will stop when the session ends.</li>
            <li>ngrok requires a free account and authentication token for public URLs.</li>
            <li>This repository is for learning purposes and experimentation.</li>
        </ul>
    </div>

    <div class="section">
        <h2>🔗 Links</h2>
        <ul>
            <li><a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI Documentation</a></li>
            <li><a href="https://ngrok.com/docs" target="_blank">Ngrok Documentation</a></li>
            <li><a href="https://www.python.org/" target="_blank">Python Official Site</a></li>
        </ul>
    </div>

    <footer>
        <p>Made with ❤️ by Mushaf | Learning FastAPI</p>
    </footer>
</body>
</html>
