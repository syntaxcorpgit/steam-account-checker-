# Steam Account Checker 🎮

A sophisticated Python tool for checking Steam account validity with advanced anti-block protection and comprehensive logging.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## ✨ Features

- **🛡️ Anti-Block Protection** - Advanced detection bypass with request rotation
- **🔄 User-Agent Rotation** - 7 different browser signatures to avoid fingerprinting
- **⚡ Multi-Threaded** - 4 concurrent workers for optimal performance
- **📊 Real-time Logging** - Comprehensive logs with colored console output
- **⏰ Smart Delays** - Variable timing (3-8s) to mimic human behavior
- **🔄 Automatic Retry** - Smart retry system with exponential backoff
- **💾 Auto-Save** - Immediate saving of working accounts
- **📈 Progress Tracking** - Live progress updates and statistics

## 🚀 Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/steam-account-checker.git
cd steam-account-checker

# Install dependencies
pip install requests

### usage
Create combo.txt with your accounts:

text
username1:password123
username2:password456
username3:password789
Run the checker:

bash
python steam_checker.py
Check results in working_accounts.txt and checker_log.txt

###📁 File Structure
text
steam-account-checker/
├── steam_checker.py          # Main script
├── combo.txt                 # Input accounts (username:password)
├── working_accounts.txt      # Output: Valid accounts
├── checker_log.txt           # Output: Detailed process log
└── README.md                 # Documentation
###🔧 How It Works
Technical Implementation
Session Management: Unique sessions with randomized headers

Request Rotation: Multiple Steam endpoints and user agents

Validation Logic: HTTP status analysis + content verification

Error Handling: Graceful failure recovery with retries

###Anti-Block Features
Random delays between requests (3-8 seconds)

7 different User-Agents (Chrome, Firefox, Edge, Safari)

Referer spoofing from popular sites

Multiple Steam public endpoints

Limited concurrent threads (4 workers)

Proper browser fingerprint simulation

### 📊 Output Examples
Console Output
text
[Account Checker] : username1 WORKING - Steam accessible
[Account Checker] : username2 NOT WORKING - Connection failed
📊 Progress: 15/100 (15.0%)
working_accounts.txt
text
username1:password123 | Status: Steam accessible | Checked: 2024-01-15 14:30:25
checker_log.txt
text
[2024-01-15 14:30:25] [Account Checker] : username1 WORKING - Steam accessible
### ⚙️ Configuration
Customizable Settings
max_workers=4 - Concurrent threads (2-6 recommended)

delay = random.uniform(3, 8) - Seconds between checks

timeout=20 - Request timeout in seconds

max_retries=2 - Retry attempts per account

### ⚠️ Legal Disclaimer
This tool is for educational purposes and legitimate account management only.

### ✅ Allowed:

Checking your own accounts

Educational and research purposes

Security testing (with permission)

### ❌ Prohibited:

Mass account checking without permission

Brute force attacks

Any illegal activities

Users are responsible for complying with Steam's Terms of Service and local laws.

### 🔧 Troubleshooting
Common Issues
Module Not Found: pip install requests

File Not Found: Ensure combo.txt exists in same directory

Connection Errors: Check internet and reduce worker count

Slow Performance: Adjust max_workers to 2-3

### Performance Estimates
Accounts	Estimated Time
10	2-5 minutes
100	25-50 minutes
1000	4-8 hours
🤝 Contributing
Contributions welcome! Please:

Fork the repository

Create a feature branch

Make your changes

Test thoroughly

Submit a pull request

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
