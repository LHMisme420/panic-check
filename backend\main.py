from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fear_engine import analyze_fear
from calm_rewrite import rewrite_calm

app = FastAPI(title="PanicCheck API", version="0.2")

# CORS — ALLOW EVERYTHING (Chrome extensions need this)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Chrome extensions WILL fail without this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputText(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: InputText):
    fear_data = analyze_fear(input.text)
    calm_version = rewrite_calm(input.text)

    return {
        "fear_score": fear_data["fear_score"],
        "triggers": fear_data["triggers"],
        "warning": fear_data["fear_score"] >= 40,
        "calm_version": calm_version
    }
