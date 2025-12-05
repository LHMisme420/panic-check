from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
import json
from dotenv import load_dotenv
from cachetools import TTLCache
import asyncio

load_dotenv()

app = FastAPI(title="PanicCheck v2 Backend")
cache = TTLCache(maxsize=500, ttl=3600)  # 1-hour cache

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

class AnalyzeRequest(BaseModel):
    text: str
    url: str = ""

async def groq_chat(messages):
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer ${GROQ_API_KEY}"},
            json={
                "model": "llama-3.1-70b-versatile",
                "messages": messages,
                "temperature": 0.3,
                "max_tokens": 1024
            },
            timeout=20.0
        )
        return r.json()["choices"][0]["message"]["content"]

async def tavily_search(query: str):
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.tavily.com/search",
            json={"api_key": TAVILY_API_KEY, "query": query, "max_results": 5},
            timeout=10.0
        )
        return r.json()

@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    text_hash = hash(req.text[:500])
    if text_hash in cache:
        return cache[text_hash]

    # Step 1: Fear & Claim Extraction
    fear_prompt = f"""
    You are PanicCheck — the ultimate fear-mongering detector.
    Analyze the text below and return ONLY valid JSON:

    {{
      "fear_score": 0-100 number (how alarmist),
      "claims": ["claim one", "claim two", ...],
      "fear_triggers": ["word/phrase", ...],
      "tone": "neutral|alarmist|panic|doomsday"
    }}

    Text: {req.text[:15000]}
    """
    try:
        raw = await groq_chat([{"role": "user", "content": fear_prompt}])
        data = json.loads(raw)
    except:
        data = {"fear_score": 75, "claims": [], "fear_triggers": ["error"], "tone": "panic"}

    # Step 2: Fact-check top 3 claims
    evidence = 0
    checked = []
    for claim in data["claims"][:3]:
        results = await tavily_search(f"fact check: {claim}")
        support = any("debunked" not in r["content"].lower() and "false" not in r["content"].lower() for r in results["results"])
        evidence += 1 if support else 0
        checked.append({"claim": claim, "supported": support})

    evidence_pct = int((evidence / max(1, len(checked))) * 100)

    result = {
        "fear_score": data["fear_score"],
        "evidence_percentage": evidence_pct,
        "tone": data["tone"],
        "triggers": data["fear_triggers"],
        "checked_claims": checked,
        "needs_warning": data["fear_score"] > 65 and evidence_pct < 60
    }

    cache[text_hash] = result
    return result

@app.post("/calm-rewrite")
async def calm_rewrite(req: AnalyzeRequest):
    prompt = open("prompt_templates/calm_rewrite.txt").read() + req.text[:20000]
    calm_text = await groq_chat([{"role": "user", "content": prompt}])
    return {"calm_version": calm_text}
