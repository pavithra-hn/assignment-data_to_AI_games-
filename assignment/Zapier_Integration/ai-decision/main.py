from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()

class Event(BaseModel):
    text: str

# 1. Configure Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

genai.configure(api_key=api_key)

# Using the model found in your list
model = genai.GenerativeModel('gemini-2.0-flash')

@app.post("/decide")
async def decide(event: Event):
    try:
        # 2. Define the Prompt
        prompt = f"""
        You are an AI router.
        Based on the event below, decide ONE action:
        - "calendar" -> meeting / schedule / call
        - "email" -> needs reply or notification
        - "ignore" -> no action needed

        Event: {event.text}

        Return ONLY one word: calendar, email, or ignore.
        """

        # 3. Generate Content
        response = model.generate_content(prompt)
        
        # Clean up response
        decision_text = response.text.strip().lower()

        # Normalize output
        if "calendar" in decision_text:
            final_decision = "calendar"
        elif "email" in decision_text:
            final_decision = "email"
        else:
            final_decision = "ignore"
            
        return {"decision": final_decision}
        
    except Exception as e:
        error_msg = str(e)
        # Handle Rate Limit specifically
        if "429" in error_msg:
            print("⚠️ Rate Limit Hit!")
            return {"decision": "ignore", "error": "Rate limit reached. Please wait a minute."}
            
        print(f"❌ Error: {error_msg}")
        return {"decision": "ignore", "error": error_msg}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
