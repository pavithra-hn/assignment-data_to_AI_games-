import requests
import json
import time

URL = "http://localhost:8000/ask"

def test_query(query):
    print(f"\n🔹 USER: {query}")
    try:
        response = requests.post(URL, json={"query": query})
        print(f"🔸 AI RESPONSE: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🤖 Testing Digital Employee PoC...")
    
    # Test 1: Calendar
    test_query("Do I have any meetings today?")
    
    time.sleep(2)
    
    # Test 2: Email
    test_query("Check my unread emails please")
