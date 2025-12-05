from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_text(input: TextInput):
    # Simple fear keywords + LLM call (you can swap for Ollama/Groq/OpenAI)
    fear_keywords = ["doomed", "collapse", "extinction", "deadly outbreak", "war", "crisis", "you will lose everything"]
    fear_count = sum(word in input.text.lower() for word in fear_keywords)
    fear_score = min(100, 30 + fear_count * 12)

    # Dummy evidence check — replace with Tavily + fact-check APIs
    evidence_percentage = 15 if fear_score > 80 else 45

    return {
        "fear_score": fear_score,
        "evidence_percentage": evidence_percentage,
        "warning": fear_score > 70
    }
