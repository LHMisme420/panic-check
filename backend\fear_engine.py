@"
import re

FEAR_KEYWORDS = {
    "collapse": 10,
    "crisis": 9,
    "panic": 9,
    "catastrophe": 10,
    "emergency": 8,
    "breaking": 6,
    "disaster": 9,
    "war": 8,
    "death": 10,
    "experts warn": 7,
    "without warning": 7,
    "immediately": 6,
    "terrifying": 10,
    "devastating": 9
}

def analyze_fear(text: str):
    text_lower = text.lower()
    score = 0
    triggers = []

    for phrase, weight in FEAR_KEYWORDS.items():
        matches = len(re.findall(phrase, text_lower))
        if matches > 0:
            score += matches * weight
            triggers.append(phrase)

    score = min(score, 100)

    return {
        "fear_score": score,
        "triggers": list(set(triggers))
    }
"@ | Set-Content backend\fear_engine.py
