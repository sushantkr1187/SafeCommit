# SafeCommit

A lightweight, cross-platform Python CLI that scans projects for exposed API keys, credentials, tokens, connection strings, private keys, and other sensitive information **before you commit**.

Prevent accidentally leaking secrets to Git repositories with fast, recursive, regex-based scanning.

---

## Features

- 🔍 Detects **25+ common secret types**
- 📂 Recursive project scanning
- ⚡ Fast regex-based detection
- 🖥️ Cross-platform (Windows, Linux, macOS)
- 🎨 Beautiful terminal output powered by Rich
- 📄 Reports file path, line number, severity, matched pattern, and matched value
- 📦 Lightweight with zero external services
- 🚀 Simple installation using `pip`

---

## Installation

Install from PyPI:

```bash
pip install safecommit-cli
```

Verify installation:

```bash
safecommit --version
```

---

## Quick Start

Scan the current project:

```bash
safecommit scan .
```

Scan another directory:

```bash
safecommit scan /path/to/project
```

Example:

```bash
safecommit scan D:\Projects\MyApp
```

---

## Example Output

```text
Scanning: D:\Projects\MyApp

Found 2 potential issue(s).

╭──────────── Secret Detected ────────────╮
│ File      : backend/config.py           │
│ Line      : 18                          │
│ Severity  : HIGH                        │
│ Pattern   : OpenAI API Key              │
│ Match     : sk-proj-****************    │
╰─────────────────────────────────────────╯
```

---

## Supported Secret Types

### API Keys & Tokens

- OpenAI API Keys
- GitHub Personal Access Tokens
- AWS Access Keys
- AWS Secret Access Keys
- Google API Keys
- Google OAuth Tokens
- Stripe Secret Keys
- Stripe Restricted Keys
- Twilio API Keys
- Slack Tokens
- Discord Bot Tokens
- Firebase Cloud Messaging Server Keys
- SendGrid API Keys

### Database Credentials

- MongoDB URIs
- PostgreSQL URIs
- MySQL URIs
- Redis URIs

### Authentication & Secrets

- JWT Tokens
- Bearer Tokens
- Hardcoded Passwords
- Hardcoded Secrets
- Hardcoded API Keys
- Hardcoded Token Variables

### Private Keys & Certificates

- RSA Private Keys
- EC Private Keys
- DSA Private Keys
- OpenSSH Private Keys
- PGP Private Keys
- X.509 Certificates

### Cloud Credentials

- Azure Storage Connection Strings
- Heroku API Keys

---

## Project Structure

```text
SafeCommit/
│
├── src/
│   └── safecommit/
│       ├── __init__.py
│       ├── cli.py
│       ├── scanner.py
│       ├── patterns.py
│       └── utils.py
│
├── tests/
├── documentation.pdf
├── README.md
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml
└── .gitignore
```

---

## Contributing

Contributions, bug reports, feature requests, and improvements are welcome.

If you'd like to contribute, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the **MIT License**.

---

## Author

**Sushant Kumar Kushwaha**

GitHub: **https://github.com/sushantkr1187**
