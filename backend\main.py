@"
from fastapi import FastAPI
from pydantic import BaseModel
from fear_engine import analyze_fear
from calm_rewrite import rewrite_calm

app = FastAPI(title="PanicCheck API", version="0.1")

class InputText(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: InputText):
    fear_data = analyze_fear(input.text)
    calm_version = rewrite_calm(input.text)

    return {
        "fear_score": fear_data["fear_score"],
        "flagged_phrases": fear_data["triggers"],
        "calm_version": calm_version,
        "warning": fear_data["fear_score"] > 60
    }
"@ | Set-Content backend\main.py
