import os
import requests
import uvicorn
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

app = FastAPI(title="Digital Employee Brain")

# --- Configuration ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ZAPIER_CALENDAR_HOOK = os.getenv("ZAPIER_CALENDAR_HOOK")
ZAPIER_EMAIL_HOOK = os.getenv("ZAPIER_EMAIL_HOOK")

if not GOOGLE_API_KEY:
    print("WARNING: GOOGLE_API_KEY is missing via .env")

# --- AI Definitions ---

class UserQuery(BaseModel):
    query: str

class IntentSchema(BaseModel):
    intent: str = Field(description="The classification of the user's intent. Must be 'check_calendar' or 'summarize_email' or 'unknown'")
    parameters: str = Field(description="Any specific parameters to pass to the tool, e.g., 'today', 'unread', 'from boss'")

def analyze_intent(query: str):
    """
    Uses Gemini to decide if the user wants to check calendar or email.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GOOGLE_API_KEY)
    
    # We use structured output to get ensuring reliable JSON parsing
    structured_llm = llm.with_structured_output(IntentSchema)
    
    prompt = f"""
    You are a digital executive assistant.
    Classify the following user query into one of these intents:
    1. check_calendar (e.g., "Do I have meetings?", "What is on my schedule?", "Am I free at 2pm?")
    2. summarize_email (e.g., "Check my emails", "Any new messages?", "Summarize inbox")
    3. unknown (if it doesn't match)

    User Query: "{query}"
    """
    
    result = structured_llm.invoke(prompt)
    return result

# --- Routes ---

@app.post("/ask")
async def ask_employee(user_query: UserQuery):
    print(f"🧠 Receiving query: {user_query.query}")
    
    # 1. Analyze Intent
    try:
        decision = analyze_intent(user_query.query)
        print(f"🤔 AI Decision: {decision.intent} | Params: {decision.parameters}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")

    # 2. Route to Zapier
    webhook_url = None
    payload = {"query": user_query.query, "ai_notes": decision.parameters}

    if decision.intent == "check_calendar":
        webhook_url = ZAPIER_CALENDAR_HOOK
    elif decision.intent == "summarize_email":
        webhook_url = ZAPIER_EMAIL_HOOK
    else:
        return {"status": "ignored", "message": "I'm sorry, I can only help with Calendar or Email right now."}

    # 3. Execute Webhook
    if webhook_url:
        if "hooks.zapier.com" not in webhook_url:
             return {"status": "simulated", "message": f"Would have called Zapier for {decision.intent}, but URL is not configured."}
             
        try:
            response = requests.post(webhook_url, json=payload)
            return {
                "status": "success", 
                "intent": decision.intent, 
                "zapier_response": response.text,
                "message": "I have instructed Zapier to process your request. You should receive an email shortly."
            }
        except Exception as e:
            return {"status": "error", "message": f"Failed to call Zapier: {str(e)}"}
            
    return {"status": "error", "message": "Configuration error: Webhook URL missing."}

if __name__ == "__main__":
    print("🚀 Starting Digital Employee Brain on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
