document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("analyze");
  const result = document.getElementById("result");

  btn.addEventListener("click", () => {
    result.innerText = "Analyzing...";

    chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
      chrome.scripting.executeScript(
        {
          target: { tabId: tabs[0].id },
          func: () => document.body.innerText
        },
        res => {
          const text = res[0].result;

          fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
          })
            .then(r => r.json())
            .then(data => {
              result.innerText =
                `Fear Score: ${data.fear_score}\n` +
                `Triggers: ${data.triggers.join(", ")}\n` +
                `Warning: ${data.warning}\n\n` +
                `Calm Version:\n${data.calm_version}`;
            })
            .catch(err => {
              result.innerText = "ERROR: " + err;
            });
        }
      );
    });
  });
});
