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
