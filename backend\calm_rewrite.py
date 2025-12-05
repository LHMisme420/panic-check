def rewrite_calm(text: str):
    replacements = {
        "panic": "concern",
        "terrifying": "serious but manageable",
        "emergency": "urgent situation",
        "crisis": "issue",
        "collapse": "decline",
    }

    new_text = text
    for k, v in replacements.items():
        new_text = new_text.replace(k, v)

    return new_text
