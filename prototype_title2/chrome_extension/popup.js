document.addEventListener("DOMContentLoaded", () => {
  const urlInput = document.getElementById("url-input");
  const scanBtn = document.getElementById("scan-btn");
  const resultsDiv = document.getElementById("results");
  const verdictBox = document.getElementById("verdict-box");
  const probPct = document.getElementById("prob-pct");
  const verdictLabel = document.getElementById("verdict-label");
  const heatmapText = document.getElementById("heatmap-text");

  const suspiciousTlds = ["tk", "ml", "cf", "gq", "cc", "xyz", "club", "online", "site", "top"];
  const keywords = ["gcash", "paymaya", "maya", "login", "verify", "verification", "activation", "bdo", "bpi"];

  if (typeof chrome !== 'undefined' && chrome.tabs && chrome.tabs.query) {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
      if (tabs && tabs[0]) {
        urlInput.value = tabs[0].url;
        runScan(tabs[0].url);
      }
    });
  } else {
    const mockUrl = "https://secure-login-portal-gcash.xyz/activation";
    urlInput.value = mockUrl;
    runScan(mockUrl);
  }

  function runScan(url) {
    if (!url) return;
    
    let score = 0.05;
    const lowerUrl = url.toLowerCase();
    
    if (url.length > 60) score += 0.15;
    
    let matched = 0;
    keywords.forEach(kw => {
      if (lowerUrl.includes(kw)) {
        score += 0.35;
        matched++;
      }
    });

    suspiciousTlds.forEach(tld => {
      if (lowerUrl.endsWith("." + tld) || lowerUrl.includes("." + tld + "/")) {
        score += 0.25;
      }
    });

    score = Math.min(score, 0.99);
    score = Math.max(score, 0.01);
    
    const isMalicious = score > 0.5;
    
    probPct.textContent = `${Math.round(score * 100)}%`;
    if (isMalicious) {
      verdictLabel.textContent = "MALICIOUS THREAT DETECTED";
      verdictLabel.style.color = "#ff3366";
      verdictBox.className = "verdict-card danger";
    } else {
      verdictLabel.textContent = "URL SECURE";
      verdictLabel.style.color = "#39e09b";
      verdictBox.className = "verdict-card safe";
    }

    heatmapText.innerHTML = "";
    for (let i = 0; i < url.length; i++) {
      const char = url[i];
      let bg = "rgba(0, 242, 254, 0.05)";
      let color = "#fff";
      
      let isSus = false;
      keywords.forEach(kw => {
        if (lowerUrl.substring(Math.max(0, i-kw.length), i+kw.length).includes(kw)) {
          isSus = true;
        }
      });
      
      if (isSus) {
        bg = "rgba(255, 8, 68, 0.25)";
        color = "#ff3366";
      }

      const span = document.createElement("span");
      span.className = "char";
      span.textContent = char;
      span.style.backgroundColor = bg;
      span.style.color = color;
      heatmapText.appendChild(span);
    }

    resultsDiv.classList.remove("hidden");
  }

  scanBtn.addEventListener("click", () => {
    runScan(urlInput.value);
  });
});
