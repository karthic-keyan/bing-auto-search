<!-- @format -->


# 🚀 Daily Bing Search Automation

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-blue?logo=github-actions)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.15.0-green?logo=selenium)
![Status](https://img.shields.io/badge/Status-Active-success)

Automated daily Bing searches to maximize Microsoft Rewards points using GitHub Actions. This project runs completely free on GitHub's infrastructure and performs 30 searches daily without requiring any server maintenance.

## ✨ Features

- 🔄 **Fully Automated**: Runs daily at 9:00 AM IST using GitHub Actions
- 💰 **100% Free**: No server costs - runs entirely on GitHub's free tier
- 🔐 **Secure**: Credentials stored safely using GitHub Secrets
- 📊 **Smart Searching**: 20 diverse topics with random selection
- ⏱️ **Realistic Delays**: Random intervals between searches (3-8 seconds)
- 📈 **Rewards Tracking**: Automatic points checking and reporting
- 🛡️ **Error Handling**: Robust error recovery and detailed logging
- 📱 **Headless Operation**: Runs invisibly without GUI

## 🏗️ Architecture

┌─────────────────┐ ┌──────────────────┐ ┌─────────────────┐
│ GitHub Actions │───▶│ Python Script │───▶│ Bing.com │
│ (Scheduler) │ │ (Selenium) │ │ (Searches) │
└─────────────────┘ └──────────────────┘ └─────────────────┘
│ │ │
▼ ▼ ▼
┌─────────────────┐ ┌──────────────────┐ ┌─────────────────┐
│ Cron Timer │ │ Chrome Browser │ │ Microsoft Login │
│ (Daily 9 AM) │ │ (Headless) │ │ (Secure Auth) │
└─────────────────┘ └──────────────────┘ └─────────────────┘



## 🚀 Quick Start

### Prerequisites

- GitHub account
- Microsoft Outlook/Hotmail account
- Basic understanding of GitHub repositories

### 1. Fork or Create Repository

**Option A: Fork this repository**


# Click "Fork" button on GitHub to copy this repository



**Option B: Create from scratch**


# Create new repository on GitHub

git clone https://github.com/YOUR_USERNAME/bing-search-automation.git
cd bing-search-automation



### 2. Set Up Repository Structure

Create these files in your repository:



bing-search-automation/
├── .github/
│ └── workflows/
│ └── daily-bing-search.yml
├── bing_search.py
├── requirements.txt
├── README.md
└── LICENSE



### 3. Configure GitHub Secrets

1. **Navigate to**: Repository → Settings → Secrets and variables → Actions
2. **Add Repository Secrets**:
   - **`OUTLOOK_USERNAME`**: Your Microsoft account email
   - **`OUTLOOK_PASSWORD`**: Your account password (or App Password)

⚠️ **Security Note**: Use App Passwords if 2FA is enabled on your Microsoft account

### 4. Deploy and Test

1. **Commit all files** to the main branch
2. **Go to Actions tab** → Find "Daily Bing Search Automation"
3. **Click "Run workflow"** for manual testing
4. **Check logs** for successful execution

## 📋 File Descriptions

### `bing_search.py`
Core automation script containing:
- **Microsoft account authentication**
- **Bing search execution with 20+ topics**
- **Random delay implementation**
- **Rewards points tracking**
- **Comprehensive error handling**

### `.github/workflows/daily-bing-search.yml`
GitHub Actions workflow that:
- **Schedules daily execution** at 9:00 AM IST
- **Sets up Chrome and ChromeDriver** automatically
- **Installs Python dependencies**
- **Runs the automation script securely**
- **Handles failures** with detailed logging

### `requirements.txt`
Python dependencies:


selenium==4.15.0



## ⚙️ Configuration

### Search Topics
Customize the search topics in `bing_search.py`:



self.search_topics = [
"Python programming tutorials",
"Your custom topic here",
# Add more topics...
]



### Scheduling
Modify the cron schedule in the workflow file:



schedule:

- cron: '30 3 \* \* \*' # 9:00 AM IST daily

# Custom schedules:

# - cron: '0 4 \* \* \*' # 9:30 AM IST

# - cron: '0 _/6 _ \* \*' # Every 6 hours



### Search Count
Adjust the number of daily searches:



searches_completed = self.perform_bing_searches(30) # Change 30 to desired count



## 📊 Monitoring & Logs

### Viewing Execution Status
1. **Actions Tab**: View all workflow runs and their status
2. **Individual Run**: Click any run to see detailed step-by-step logs
3. **Search Summary**: Each run shows completed searches and points earned

### Log Output Example


🚀 Starting Bing Search Automation
📅 Running for user: use**_@outlook.com
✅ Chrome driver setup completed with Selenium Manager
🔐 Starting Microsoft account login...
📧 Entered username: use_**
🔑 Password entered
✅ Microsoft login completed successfully
🔍 Starting 30 Bing searches...
🔎 Search 1/30: Python programming tutorials
⏳ Waiting 5.2 seconds...

✅ Completed 30 searches successfully
📊 Checking Microsoft Rewards points...
🎯 Current points: 8,450
=====================================
📈 AUTOMATION SUMMARY
✅ Searches completed: 30
🎯 Current points: 8,450
🎉 Daily Bing search automation completed successfully!
=====================================



## 🔧 Troubleshooting

### Common Issues

**Workflow not showing in Actions tab**
- Ensure files are on the main branch
- Check YAML syntax for errors
- File must be in `.github/workflows/` directory

**Login failures**
- Verify credentials in GitHub Secrets
- Use App Password if 2FA is enabled
- Check for account lockouts

**ChromeDriver issues**
- The workflow handles this automatically
- Check logs for specific Chrome-related errors

**Search failures**
- Network timeouts are handled with retries
- Script includes delays to avoid rate limiting

### Debug Mode
Enable verbose logging by modifying the Python script:



import logging
logging.basicConfig(level=logging.DEBUG)



## 🛡️ Security Best Practices

- ✅ **Store credentials** in GitHub Secrets (never in code)
- ✅ **Use App Passwords** instead of main account password
- ✅ **Keep repository private** to protect automation details
- ✅ **Regular secret rotation** for enhanced security
- ✅ **Monitor execution logs** for suspicious activity

## 📈 Performance & Limitations

### GitHub Actions Limits
- **Free tier**: 2,000 minutes/month for private repos
- **Public repos**: Unlimited free minutes
- **Concurrent jobs**: Limited based on plan
- **Workflow timeout**: Maximum 6 hours per job

### Automation Performance
- **Execution time**: ~5-8 minutes per run
- **Success rate**: 95%+ with error handling
- **Daily searches**: Up to 30 (configurable)
- **Resource usage**: Minimal (headless browser)

## 🤝 Contributing

1. **Fork** the repository
2. **Create feature branch**: `git checkout -b feature-name`
3. **Make changes** and test thoroughly
4. **Submit pull request** with detailed description

### Development Setup


# Clone repository

git clone https://github.com/YOUR_USERNAME/bing-search-automation.git
cd bing-search-automation

# Install dependencies

pip install -r requirements.txt

# Run locally (with environment variables)

export OUTLOOK_USERNAME="your-email@outlook.com"
export OUTLOOK_PASSWORD="your-password"
python bing_search.py



## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This automation tool is for educational purposes. Users are responsible for:
- **Complying** with Microsoft's Terms of Service
- **Responsible usage** to avoid account restrictions
- **Understanding** that automation may violate platform policies

**Use at your own discretion and risk.**

## 🙋‍♀️ Support

- **Issues**: [Create an issue](../../issues) for bugs or feature requests
- **Discussions**: [Join discussions](../../discussions) for general questions
- **Security**: Report security vulnerabilities privately

## 🏆 Acknowledgments

- **Selenium WebDriver** for browser automation
- **GitHub Actions** for free CI/CD infrastructure
- **Microsoft Rewards** program for the opportunity
- **Open source community** for tools and inspiration

---

**⭐ If this project helped you earn more rewards points, please consider starring the repository!**


markdown
# Contributing to Daily Bing Search Automation

Thank you for considering contributing to this project! Here are some guidelines to help you get started.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request

## Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

### Testing

- Test all changes locally before submitting
- Ensure GitHub Actions workflow passes
- Test with different Microsoft account types

### Commit Messages

- Use clear, descriptive commit messages
- Start with a capital letter
- Use present tense ("Add feature" not "Added feature")

## Reporting Issues

When reporting issues, please include:

- Operating system details
- Python version
- Error messages and logs
- Steps to reproduce

## Security

Never commit sensitive information like:

- Passwords or API keys
- Personal email addresses
- Account credentials

Use GitHub Secrets for sensitive data.
