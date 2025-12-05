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
