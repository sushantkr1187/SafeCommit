# SafeCommit

**Detect exposed secrets before they reach your Git repository.**

A lightweight, cross-platform Python CLI that scans projects for exposed API keys, credentials, tokens, connection strings, private keys, and other sensitive information **before you commit**.

Built for developers who want an additional security check before committing code, SafeCommit uses pattern-based detection to identify potential secrets and report their locations.

<p align="center">

[![PyPI](https://img.shields.io/pypi/v/safecommit-cli?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/safecommit-cli/)
[![Python](https://img.shields.io/pypi/pyversions/safecommit-cli?logo=python&logoColor=white)](https://pypi.org/project/safecommit-cli/)
[![License: MIT](https://img.shields.io/github/license/sushantkr1187/SafeCommit?color=green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/sushantkr1187/SafeCommit?style=social)](https://github.com/sushantkr1187/SafeCommit/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/sushantkr1187/SafeCommit)](https://github.com/sushantkr1187/SafeCommit/issues)
[![GitHub Release](https://img.shields.io/github/v/release/sushantkr1187/SafeCommit?include_prereleases)](https://github.com/sushantkr1187/SafeCommit/releases)

</p>

---

## Overview

Credentials accidentally committed to source control can expose applications, infrastructure, databases, and third-party services.

SafeCommit helps developers identify potential credential leaks by scanning project files before they are committed.

### Why SafeCommit?

- **Security-focused:** Detects patterns associated with commonly exposed credentials and secrets.
- **Developer-friendly:** Simple command-line interface with readable terminal output.
- **Lightweight:** Python-based scanning without requiring external security services.
- **Cross-platform:** Designed for Windows, Linux, and macOS.
- **Flexible:** Supports recursive scanning and directory exclusion.
- **Automation-ready:** JSON output enables integration with scripts and other tools.

---

## Features

| Feature | Description |
|---|---|
| Secret Detection | Detects 35+ common secret detection patterns |
| Recursive Scanning | Scans project directories and supported files |
| Regex Engine | Uses pattern-based matching to identify potential secrets |
| Directory Exclusion | Excludes specified directories from scanning |
| JSON Output | Produces structured scan results |
| Rich Terminal Output | Presents findings using Rich |
| Finding Details | Reports file path, line number, severity, pattern, and matched value |
| File Filtering | Skips unsupported and ignored files |
| File Size Limit | Skips files exceeding the configured 20 MB scanner limit |
| Cross-platform | Supports Windows, Linux, and macOS |
| Lightweight | No external service required for scanning |

---

# What SafeCommit does
- Scans project files for potential secrets.
- Reports matching patterns and locations.
- Helps developers identify credentials before committing.

---

## Installation

SafeCommit is available on PyPI as `safecommit-cli`

### Requirements

- Python version supported by the package
- `pip`

Install from PyPI:

```bash
pip install safecommit-cli
```

Verify installation:

```bash
safecommit --version
```
or
```bash
safecommit -v
```

> The displayed version depends on the version installed in your environment.

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

- JSON Web Tokens (JWT)
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

> Detection coverage depends on the patterns implemented in the installed version. The list above describes supported categories, not a guarantee that every credential format or provider-specific variation will be detected.

---

> SafeCommit uses pattern-based detection to identify potential secrets. Detection results may include false positives, and the absence of findings does not guarantee that a project is free of exposed credentials.

---

## How It Works

SafeCommit follows a straightforward scanning workflow:

1. **Directory Traversal:** Recursively examines the specified project directory.
2. **File Filtering:** Skips ignored files, unsupported file types, and files exceeding the configured size limit.
3. **Pattern Matching:** Applies regular expressions to supported file contents.
4. **Finding Collection:** Records potential matches with their file path, line number, severity, pattern name, and matched value.
5. **Reporting:** Displays findings in the terminal or produces structured JSON output.

SafeCommit is designed to help developers review potential exposures before committing code.

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
├── .gitattributes
└── .gitignore
```

### Core Modules

| Module | Responsibility |
|---|---|
| `cli.py` | Command-line interface and scan output |
| `scanner.py` | Directory traversal and pattern detection |
| `patterns.py` | Secret detection patterns |
| `utils.py` | File filtering, ignore rules, and file reading |

---

## Development

### Clone the repository

```bash
git clone https://github.com/sushantkr1187/SafeCommit.git
```

### Navigate to the project

```bash
cd SafeCommit
```

### Create a virtual environment

Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install the project

```bash
python -m pip install -e .
```

### Run SafeCommit

```bash
safecommit scan .
```

---

## Security Considerations

SafeCommit uses regex-based detection to identify potential secrets.

Pattern-based detection has inherent limitations:

- **False positives:** Ordinary strings may match a secret detection pattern.
- **False negatives:** Credentials may not match known patterns.
- **Format variation:** Provider-specific formats can change.
- **Context limitations:** A matching string does not necessarily indicate an active credential.

SafeCommit is a supplementary security tool, not a complete secret-management or security-audit solution.

### Recommended practices

- Never commit real credentials intentionally.
- Use environment variables or dedicated secret-management systems.
- Rotate credentials if they have been exposed.
- Review findings before sharing scan output.
- Use additional security checks where appropriate.
- Do not rely exclusively on SafeCommit to guarantee that a repository contains no secrets. 

> SafeCommit is actively being developed and improved. We are continuously working to expand detection coverage, refine existing patterns, reduce false positives, and improve the overall reliability and accuracy of the tool. While no pattern-based scanner can guarantee complete detection, we are committed to making SafeCommit more dependable, effective, and useful for developers with every improvement and release.
> Your feedback, bug reports, and contributions help us make SafeCommit better.

---

## Contributing

Contributions, bug reports, feature requests, and improvements are always welcome.

You can contribute by:

- Reporting bugs
- Suggesting new detection patterns
- Improving existing regex coverage
- Adding test cases
- Improving documentation
- Submitting pull requests

### Contribution Workflow

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Add or update tests.
5. Submit a pull request.

Repository:

https://github.com/sushantkr1187/SafeCommit

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history and notable changes.

---

## License

This project is licensed under the **MIT License**.
See [LICENSE](LICENSE) for details.

---

## Author

**Sushant Kumar Kushwaha**

GitHub: [@sushantkr1187](https://github.com/sushantkr1187)

---

## Links

- **GitHub Repository:** https://github.com/sushantkr1187/SafeCommit
- **PyPI Package:** https://pypi.org/project/safecommit-cli/
- **Issues:** https://github.com/sushantkr1187/SafeCommit/issues
- **Releases:** https://github.com/sushantkr1187/SafeCommit/releases
- **Changelog:** [CHANGELOG.md](CHANGELOG.md)

---

<p align="center"> 

**Built with Python. Designed for safer commits.**

</p>
