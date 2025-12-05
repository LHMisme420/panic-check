import re

TRIGGERS = [
    "catastrophic", "panic", "emergency", "immediately",
    "crisis", "terrifying", "collapse", "horrifying",
    "danger", "breaking", "alert", "worst case",
]

def analyze_fear(text: str):
    text_lower = text.lower()
    found = [t for t in TRIGGERS if t in text_lower]

    fear_score = min(len(found) * 10, 100)

    return {
        "fear_score": fear_score,
        "triggers": found
    }
