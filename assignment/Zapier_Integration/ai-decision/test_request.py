import requests

url = "http://localhost:8000/decide"
data = {"text": "I need to schedule a meeting for tomorrow at 2pm"}

try:
    response = requests.post(url, json=data)
    print(response.json())
except Exception as e:
    print(f"Error: {e}")
