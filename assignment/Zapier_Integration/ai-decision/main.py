import os
from typing import Annotated, TypedDict, Union
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# LangChain & LangGraph imports
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, END

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

app = FastAPI(title="Advanced AI Decision Server (LangGraph)")

# 1. Define the State
class AgentState(TypedDict):
    text: str
    context: str
    decision: str

# 2. Define the Nodes
def mcp_context_node(state: AgentState):
    """
    Simulates MCP (Model Context Protocol).
    In a real MCP setup, this would query a separate MCP server.
    Here, we read local project context to 'enrich' the AI's understanding.
    """
    # Simulate reading local documentation for context
    # This helps the AI understand what 'calendar' or 'email' means for this project.
    context = (
        "Project Context: This is a Zapier routing tool. "
        "Categories: 'calendar' (for meetings/schedules), "
        "'email' (for requests/messages), 'ignore' (for everything else). "
    )
    return {"context": context}

def decide_node(state: AgentState):
    """
    Uses LangChain to make the final decision.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)
    
    prompt = f"""
    You are an AI Routing Agent.
    INPUT TEXT: "{state['text']}"
    REFERENCE CONTEXT: {state['context']}
    
    TASK: Decide if this text belongs to 'calendar', 'email', or 'ignore'.
    RULES:
    - Respond with ONLY the word: 'calendar', 'email', or 'ignore'.
    - Do not include punctuation or explanations.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    decision = response.content.strip().lower()
    
    # Fallback/Safety Check
    if decision not in ['calendar', 'email', 'ignore']:
        decision = 'ignore'
        
    return {"decision": decision}

# 3. Build the Graph
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("enrich_context", mcp_context_node)
workflow.add_node("classify", decide_node)

# Add Edges
workflow.set_entry_point("enrich_context")
workflow.add_edge("enrich_context", "classify")
workflow.add_edge("classify", END)

# Compile the Graph
runnable = workflow.compile()

# --- FastAPI Integration ---

class Event(BaseModel):
    text: str

@app.post("/decide")
async def decide(event: Event):
    try:
        # Run the LangGraph
        initial_state = {"text": event.text, "context": "", "decision": ""}
        result = runnable.invoke(initial_state)
        
        return {"decision": result["decision"]}
    except Exception as e:
        # Basic error handling for rate limits etc.
        if "429" in str(e):
            return {"decision": "ignore", "error": "Rate limit reached. Please wait a minute."}
        return {"decision": "ignore", "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
