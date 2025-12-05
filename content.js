// Inject warning banner when page is scary enough
async function checkPage() {
  const text = document.body.innerText;
  const response = await fetch('http://localhost:8000/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: text.substring(0, 20000) })
  });
  
  const result = await response.json();
  
  if (result.fear_score > 70) {
    const banner = document.createElement('div');
    banner.innerHTML = `
      <div style="position:fixed;top:0;left:0;right:0;z-index:99999;
                  background:#ff2d2d;color:white;padding:15px 20px;
                  font-family:sans-serif;font-size:18px;font-weight:bold;
                  text-align:center;box-shadow:0 4px 20px rgba(0,0,0,0.5);">
        🔥 PANICCHECK WARNING: High Fear-Mongering Detected (${result.fear_score}/100)<br>
        <span style="font-size:14px;font-weight:normal;">
          Only ${result.evidence_percentage}% of claims are substantiated.
        </span>
      </div>`;
    document.body.prepend(banner);
  }
}

checkPage();
async function injectPanicWarning() {
  const text = document.body.innerText;
  const url = window.location.href;

  const res = await fetch('http://localhost:8001/analyze', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({text, url})
  }).then(r => r.json());

  if (!res.needs_warning) return;

  const banner = document.createElement('div');
  banner.id = 'paniccheck-banner';
  banner.innerHTML = `
    <div style="position:fixed;top:0;left:0;right:0;z-index:999999;
                background:linear-gradient(90deg,#ff2d2d,#ff6b6b);color:white;
                padding:20px;font-family:system-ui;font-weight:bold;
                text-align:center;box-shadow:0 10px 30px rgba(0,0,0,0.6);
                animation: pulse 2s infinite;">
      ☢️ PANICCHECK EXTREME WARNING ☢️<br>
      Fear Score: ${res.fear_score}/100 | Evidence: ${res.evidence_percentage}%
      <div style="margin-top:10px;">
        <button id="calm-btn" style="background:#1a1a1a;color:white;border:none;padding:10px 20px;border-radius:8px;cursor:pointer;">
          Show Calm, Factual Version
        </button>
      </div>
    </div>
    <style>
      @keyframes pulse { 0%{opacity:0.9} 50%{opacity:1} 100%{opacity:0.9} }
    </style>
  `;
  document.body.prepend(banner);

  document.getElementById('calm-btn').onclick = async () => {
    banner.innerHTML = `<div style="padding:40px;background:#0f0f0f;color:#0f0;font-size:18px;">Generating calm version...</div>`;
    const calm = await fetch('http://localhost:8001/calm-rewrite', {
      method: 'POST', body: JSON.stringify({text, url})
    }).then(r => r.json());
    
    document.body.innerHTML = `<pre style="white-space:pre-wrap;font-family:system-ui;padding:40px;background:#0a0a0a;color:#0f0;">${calm.calm_version}</pre>`;
  };
}

injectPanicWarning();
