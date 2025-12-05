# panic-check
paniccheck/
├── README.md
├── LICENSE
├── package.json
├── manifest.json
├── background.js
├── content.js
├── popup/
│   ├── popup.html
│   ├── popup.js
│   └── style.css
├── icons/
│   ├── icon16.png
│   ├── icon48.png
│   └── icon128.png
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
└── datasets/
    └── fear_examples.jsonl   (training data seed)
    # PanicCheck 🔥🛡️

**The open-source browser extension that detects unsubstantiated fear-mongering in news and social media — in real time.**

When an article or tweet screams "WE'RE ALL DOOMED" but has zero sources — PanicCheck slaps a giant warning on it.

Live demo (Chrome/Edge/Firefox): Coming 24 hours after 100 stars ✨

### Features
- Real-time Fear Score (0–100)
- Automatic fact-check verification
- Big red warning banners when fear >>> evidence
- "Show Calm Version" button (neutral rewrite)
- Fully open-source, no censorship backdoors

### Installation (Chrome/Edge/Brave/Firefox)

1. Clone or download this repo
2. Open your browser → Extensions → Enable "Developer mode"
3. Click "Load unpacked" → select the `paniccheck` folder
4. Done! The chili pepper icon will now appear on scary articles

### Self-host the backend (optional but recommended)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Add your keys (Tavily, OpenAI/Groq/Ollama, etc.)
uvicorn app.py --reload
