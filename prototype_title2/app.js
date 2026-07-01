document.addEventListener("DOMContentLoaded", () => {
    const urlInput = document.getElementById("url-input");
    const scanBtn = document.getElementById("scan-btn");
    const resultSection = document.getElementById("result-section");
    const redirectBox = document.getElementById("redirect-box");
    const flowOrig = document.getElementById("flow-orig");
    const flowResolved = document.getElementById("flow-resolved");
    const progressValue = document.querySelector(".progress-value");
    const circularProgress = document.querySelector(".circular-progress");
    const verdict = document.getElementById("verdict");
    const verdictDesc = document.getElementById("verdict-desc");
    const heatmapText = document.getElementById("heatmap-text");
    
    // Metrics
    const mLength = document.getElementById("metric-length");
    const mDigits = document.getElementById("metric-digits");
    const mKeywords = document.getElementById("metric-keywords");
    const mTld = document.getElementById("metric-tld");
    const mEntropy = document.getElementById("metric-entropy");

    // Suspicious substrings weights
    const maliciousPatterns = {
        "gcash": 0.95,
        "paymaya": 0.90,
        "maya": 0.85,
        "login": 0.80,
        "verify": 0.85,
        "verification": 0.90,
        "activation": 0.92,
        "update": 0.70,
        "secure": 0.65,
        "signin": 0.75,
        "bdo": 0.88,
        "bpi": 0.85,
        "landbank": 0.88,
        "metrobank": 0.85,
        "sss-verification": 0.95,
        "claim-rewards": 0.94,
        "free-promo": 0.90
    };

    const suspiciousTlds = ["tk", "ml", "cf", "gq", "cc", "xyz", "club", "online", "site", "top"];

    // 1. Redirect Resolver Mock Simulation
    function checkRedirects(url) {
        const lowers = url.toLowerCase();
        if (lowers.includes("bit.ly/") || lowers.includes("tinyurl.com/") || lowers.includes("t.co/")) {
            let resolved = "https://secure-gcash-update-verification.xyz/login.php";
            if (lowers.includes("bdo")) {
                resolved = "https://bdo-online-banking-rewards-claim.club/signin";
            }
            return { redirected: true, resolved: resolved };
        }
        return { redirected: false, resolved: url };
    }

    // 2. Shannon Entropy Calculation
    function calculateEntropy(str) {
        let freq = {};
        for (let i=0; i<str.length; i++) {
            let character = str.charAt(i);
            freq[character] = (freq[character] || 0) + 1;
        }
        let entropy = 0;
        for (let character in freq) {
            let p = freq[character] / str.length;
            entropy -= p * Math.log2(p);
        }
        return entropy;
    }

    // 3. Scan Process
    function runScan(rawUrl) {
        if (!rawUrl.trim()) return;

        // Reset visual state
        resultSection.classList.add("hidden");
        redirectBox.classList.add("hidden");

        const redirectResult = checkRedirects(rawUrl);
        const urlToScan = redirectResult.resolved;

        // Show redirect logger if redirected
        if (redirectResult.redirected) {
            flowOrig.textContent = rawUrl;
            flowResolved.textContent = redirectResult.resolved;
            redirectBox.classList.remove("hidden");
        }

        const scanScore = scoreURL(urlToScan);
        renderDashboard(urlToScan, scanScore);
        resultSection.classList.remove("hidden");
    }

    // 4. Score logic based on character structure
    function scoreURL(url) {
        const lowerUrl = url.toLowerCase();
        let score = 0.05;

        if (url.length > 50) score += 0.10;
        if (url.length > 80) score += 0.15;

        let tld = getTLD(lowerUrl);
        if (suspiciousTlds.includes(tld)) {
            score += 0.25;
        }

        const dashCount = (lowerUrl.match(/-/g) || []).length;
        if (dashCount > 2) score += 0.10;
        if (dashCount > 5) score += 0.15;
        
        const dotCount = (lowerUrl.match(/\./g) || []).length;
        if (dotCount > 3) score += 0.10;

        let matches = 0;
        Object.keys(maliciousPatterns).forEach(pattern => {
            if (lowerUrl.includes(pattern)) {
                score += maliciousPatterns[pattern] * 0.4;
                matches++;
            }
        });

        score = Math.min(score, 0.994);
        score = Math.max(score, 0.012);

        return {
            probability: score,
            tld: tld,
            matches: matches
        };
    }

    function getTLD(url) {
        try {
            const hostname = url.startsWith("http") ? new URL(url).hostname : url.split('/')[0];
            const parts = hostname.split('.');
            return parts[parts.length - 1];
        } catch(e) {
            return "com";
        }
    }

    // 5. Render dashboard with animations
    function renderDashboard(url, scanResult) {
        const probPct = Math.round(scanResult.probability * 100);
        
        let progressStartValue = 0;
        let progressEndValue = probPct;
        let speed = 15;
        
        const isMalicious = scanResult.probability > 0.5;
        const activeColor = isMalicious ? "var(--glow-pink)" : "var(--glow-cyan)";
        const labelText = isMalicious ? "MALICIOUS THREAT" : "SECURE";
        const labelDesc = isMalicious 
            ? "WARNING: Character-level patterns match known phishing indicators. Accessing this site is highly discouraged."
            : "This URL contains typical features found in authentic, registered academic and commercial domains.";
            
        verdict.style.color = isMalicious ? "var(--danger-red)" : "var(--safe-green)";
        verdict.textContent = labelText;
        verdictDesc.textContent = labelDesc;

        // Clear previous interval if any
        if (window.progressInterval) {
            clearInterval(window.progressInterval);
        }

        window.progressInterval = setInterval(() => {
            if(progressStartValue >= progressEndValue) {
                clearInterval(window.progressInterval);
            } else {
                progressStartValue++;
            }
            progressValue.textContent = `${progressStartValue}%`;
            circularProgress.style.background = `conic-gradient(${activeColor} ${progressStartValue * 3.6}deg, rgba(255, 255, 255, 0.03) 0deg)`;
        }, speed);

        renderHeatmap(url);

        mLength.textContent = url.length;
        
        const digitCount = (url.match(/\d/g) || []).length;
        const letterCount = (url.match(/[a-zA-Z]/g) || []).length;
        const ratio = letterCount > 0 ? ((digitCount / letterCount) * 100).toFixed(1) : "0.0";
        mDigits.textContent = `${ratio}%`;
        
        mKeywords.textContent = scanResult.matches;
        mTld.textContent = scanResult.tld;
        mEntropy.textContent = calculateEntropy(url).toFixed(2);
    }

    // 6. Draw Heatmap (Explainable feature representation)
    function renderHeatmap(url) {
        heatmapText.innerHTML = "";
        const lowerUrl = url.toLowerCase();
        
        let weights = new Array(url.length).fill(0.05);

        let tld = getTLD(lowerUrl);
        if (suspiciousTlds.includes(tld)) {
            let tldIndex = lowerUrl.lastIndexOf(tld);
            if (tldIndex !== -1) {
                for (let i = tldIndex; i < tldIndex + tld.length; i++) {
                    weights[i] = 0.60;
                }
            }
        }

        Object.keys(maliciousPatterns).forEach(pattern => {
            let index = lowerUrl.indexOf(pattern);
            while (index !== -1) {
                for (let i = index; i < index + pattern.length; i++) {
                    weights[i] = Math.max(weights[i], maliciousPatterns[pattern]);
                }
                index = lowerUrl.indexOf(pattern, index + 1);
            }
        });

        for(let i=0; i<url.length; i++) {
            if (url[i] === '-' || url[i] === '.') {
                weights[i] = Math.max(weights[i], 0.45);
            }
        }

        for (let i = 0; i < url.length; i++) {
            const char = url[i];
            const weight = weights[i];
            
            let color = "rgba(0, 242, 254, 0.1)";
            let border = "transparent";
            let textColor = "#fff";
            
            if (weight > 0.7) {
                color = "rgba(255, 8, 68, 0.3)";
                border = "rgba(255, 8, 68, 0.6)";
                textColor = "var(--glow-pink)";
            } else if (weight > 0.3) {
                color = "rgba(127, 0, 255, 0.2)";
                border = "rgba(127, 0, 255, 0.4)";
                textColor = "#c5a3ff";
            }
            
            const span = document.createElement("span");
            span.className = "heatmap-char";
            span.textContent = char;
            span.style.backgroundColor = color;
            span.style.border = `1px solid ${border}`;
            span.style.color = textColor;
            span.title = `Index: ${i} | Char: '${char}' | Model Weight: ${weight.toFixed(2)}`;
            
            heatmapText.appendChild(span);
        }
    }

    scanBtn.addEventListener("click", () => {
        runScan(urlInput.value);
    });

    urlInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            runScan(urlInput.value);
        }
    });

    document.querySelectorAll(".example-btn").forEach(btn => {
        btn.addEventListener("click", (e) => {
            const url = e.target.getAttribute("data-url");
            urlInput.value = url;
            runScan(url);
        });
    });
});
