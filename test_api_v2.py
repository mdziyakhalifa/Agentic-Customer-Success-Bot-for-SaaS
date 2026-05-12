import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

for version in ["v1", "v1beta"]:
    for model in ["gemini-1.5-flash", "gemini-pro"]:
        url = f"https://generativelanguage.googleapis.com/{version}/models/{model}:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        data = {"contents": [{"parts": [{"text": "Hello"}]}]}
        response = requests.post(url, headers=headers, json=data)
        print(f"{version} {model}: {response.status_code}")
        if response.status_code != 200:
            print(response.json())
