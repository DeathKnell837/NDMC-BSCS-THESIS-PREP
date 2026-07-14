import json
import os
import random

def generate_url_dataset():
    benign_domains = [
        "google.com", "facebook.com", "youtube.com", "twitter.com", "instagram.com",
        "wikipedia.org", "yahoo.com", "amazon.com", "netflix.com", "reddit.com",
        "microsoft.com", "github.com", "ndmc.edu.ph", "gov.ph", "philhealth.gov.ph",
        "pagibigfund.gov.ph", "sss.gov.ph", "bdo.com.ph", "bpiexpressonline.com",
        "metrobank.com.ph", "gcash.com", "maya.ph", "lazada.com.ph", "shopee.ph",
        "zoom.us", "spotify.com", "canva.com", "stackoverflow.com", "medium.com"
    ]
    benign_paths = [
        "", "/", "/search?q=query", "/login", "/home", "/about", "/contact",
        "/index.html", "/profile/user", "/support/help", "/docs/v1/guide"
    ]
    phishing_keywords = [
        "login", "verify", "secure", "update", "signin", "account", "verification",
        "billing", "banking", "activation", "confirm", "portal", "support-service",
        "refund-claim", "rewards-claim", "gcash-activation", "bdo-online", "bpi-secure"
    ]
    suspicious_tlds = [
        "cc", "tk", "ml", "cf", "gq", "xyz", "club", "info", "top", "online", "site"
    ]
    
    dataset = []
    
    # Generate Benign URLs (Label: 0)
    for _ in range(600):
        domain = random.choice(benign_domains)
        path = random.choice(benign_paths)
        sub = "www." if random.random() > 0.5 else ""
        url = f"https://{sub}{domain}{path}"
        dataset.append({"url": url, "label": 0})
        
    # Generate Phishing URLs (Label: 1)
    for _ in range(600):
        structure_type = random.randint(1, 4)
        
        if structure_type == 1:
            brand = random.choice(["gcash", "maya", "paymaya", "gcash-card"])
            kw = random.choice(phishing_keywords)
            tld = random.choice(suspicious_tlds)
            url = f"http://{brand}-{kw}-portal.{tld}/index.php"
            
        elif structure_type == 2:
            bank = random.choice(["bdo", "bpi", "metrobank", "landbank"])
            kw = random.choice(phishing_keywords)
            tld = random.choice(suspicious_tlds)
            url = f"https://online-{bank}-{kw}.{tld}/login.html"
            
        elif structure_type == 3:
            gov = random.choice(["sss", "pagibig", "philhealth", "dilg"])
            tld = random.choice(suspicious_tlds)
            url = f"http://{gov}-member-verification-portal.{tld}/verify"
            
        else:
            words = [random.choice(phishing_keywords), "service", "security", "update"]
            random.shuffle(words)
            domain = "-".join(words[:random.randint(2, 3)])
            tld = random.choice(suspicious_tlds)
            url = f"http://{domain}.{tld}/login"
            
        dataset.append({"url": url, "label": 1})
        
    random.shuffle(dataset)
    return dataset

def main():
    print("Generating simulated local dataset of 1,200 URLs...")
    dataset = generate_url_dataset()
    
    chars = "abcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;="
    char_map = {char: idx + 1 for idx, char in enumerate(chars)}
    char_map["<UNK>"] = len(char_map) + 1
    
    output_dir = "C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/prototype_title2"
    os.makedirs(output_dir, exist_ok=True)
    
    dataset_file = os.path.join(output_dir, "url_dataset.json")
    with open(dataset_file, "w") as f:
        json.dump(dataset, f, indent=2)
        
    charmap_file = os.path.join(output_dir, "char_map.json")
    with open(charmap_file, "w") as f:
        json.dump(char_map, f, indent=2)
        
    print(f"Dataset saved to: {dataset_file}")
    print(f"Character map saved to: {charmap_file}")

if __name__ == '__main__':
    main()
