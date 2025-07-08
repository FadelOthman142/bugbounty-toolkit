# 🐞 Bug Bounty Toolkit

A Python-based reconnaissance and exploitation CLI toolkit designed to help bug bounty hunters, penetration testers, and security researchers automate common web vulnerability testing tasks.

> 🔐 Built by [Fadel  Othman](https://github.com/yourusername) — second-year Computer Engineering student and cybersecurity enthusiast.

---

## ✨ Features

- 🌐 **Subdomain Enumeration** using `crt.sh`
- 📁 **Directory Brute Force Scanner** (Wordlist-based)
- 🧪 **Payload Tester** for XSS and SQLi (GET/POST support + Async)
- 🔐 **Security Header Scanner**
- 🧰 Reusable **Utility Functions** (colors, saving, output formatting)

---

## 📂 Project Structure
bugbounty-toolkit/
├── core/ # All functional modules
│ ├── subdomain.py
│ ├── dirbrute.py
│ ├── payloadtester.py
│ ├── headerscan.py
│ └── utils.py
├── wordlists/ # Wordlists for brute-forcing
│ └── common.txt
├── output/ # (Optional) Auto-created to store scan results
├── main.py # Entry point CLI
├── requirements.txt # All required Python packages
└── README.md

---
##Legal Disclaimer:

Bug Bounty Toolkit is designed as a tool to assist security researchers and ethical hackers with reconnaissance and exploitation tasks. By using this software, you agree to the following terms:

This toolkit is intended only for authorized security testing on systems for which you have explicit permission from the owner.

You must not use this tool to attack, exploit, or compromise any systems without prior legal authorization.

The author, Fadel Othman, and any contributors are not responsible or liable for any damage, data loss, or legal consequences resulting from misuse of this tool.

Use this toolkit at your own risk.

It is your responsibility to ensure compliance with all applicable laws, regulations, and policies in your jurisdiction.

((""Unauthorized use of this toolkit may result in criminal or civil penalties"")).
---
## 🚀 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/yourusername/bugbounty-toolkit.git
cd bugbounty-toolkit

##Install Dependencies:
pip install -r requirements.txt

## ▶️ Usage
Run the toolkit:

bash
Copy code
python main.py



