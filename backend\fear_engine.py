import re

FEAR_KEYWORDS = {
    "collapse": 18,
    "crisis": 15,
    "panic": 16,
    "catastrophe": 20,
    "emergency": 14,
    "breaking": 12,
    "disaster": 17,
    "war": 16,
    "death": 20,
    "mass death": 30,
    "you are not safe": 35,
    "experts warn": 14,
    "without warning": 14,
    "imminent": 18,
    "terrifying": 18,
    "devastating": 19,
    "total collapse": 35,
    "end of the world": 40,
    "everything will change": 15
}

INTENSITY_MULTIPLIERS = {
    "total": 1.4,
    "immediate": 1.3,
    "imminent": 1.3,
    "mass": 1.4,
    "global": 1.2,
    "final": 1.5
}

def analyze_fear(text: str):
    text_lower = text.lower()
    score = 0
    triggers = []

    # Phrase scoring
    for phrase, weight
