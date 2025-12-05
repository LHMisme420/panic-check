@"
import re

REWRITE_MAP = {
    "experts warn": "analysts report",
    "panic": "concern",
    "collapse": "decline",
    "catastrophe": "serious event",
    "disaster": "major incident",
    "terrifying": "concerning",
    "devastating": "severe",
    "breaking": "update",
    "emergency": "developing situation"
}

def rewrite_calm(text: str):
    calm_text = text
    for k, v in REWRITE_MAP.items():
        calm_text = re.sub(k, v, calm_text, flags=re.IGNORECASE)
    return calm_text
"@ | Set-Content backend\calm_rewrite.py
