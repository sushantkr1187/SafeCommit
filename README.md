# SafeCommit
A cross-platform Python CLI that scans projects for exposed API keys, secrets, credentials, and sensitive information before you commit.

It recursively scans project files using pattern-based detection and reports potential security risks with file locations, line numbers, severity levels, and matched patterns.

---

## Features

- Cross-platform support (Windows, Linux, macOS)
- Recursive directory scanning
- Detects common API keys and credentials
- Detects private keys, certificates, and tokens
- Rich terminal output
- Fast regex-based scanning
- Lightweight and easy to use

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sushantkr1187/SafeCommit.git
cd SafeCommit
```

Create a virtual environment (recommended):

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install the package in editable mode:

```bash
pip install -e .
```

---

## Usage

Scan the current directory

```bash
safecommit scan .
```

Scan another project

```bash
safecommit scan /path/to/project
```

Show version

```bash
safecommit --version
```

or

```bash
safecommit -v
```

---

## Example Output

```text
Scanning: D:\Projects\MyProject

Found 2 potential issue(s).

File      : backend/config.py
Line      : 18
Severity  : HIGH
Pattern   : OpenAI API Key
Match      : sk-proj-************************
```

---

## Currently Detected

- OpenAI API Keys
- GitHub Personal Access Tokens
- AWS Access Keys
- Google API Keys
- Google OAuth Credentials
- Azure Storage Connection Strings
- Stripe API Keys
- Twilio API Keys
- Slack Tokens
- Discord Tokens
- JWT Tokens
- Bearer Tokens
- MongoDB URIs
- PostgreSQL URIs
- MySQL URIs
- Redis URIs
- Hardcoded Passwords
- Private Keys
- SSH Keys
- PGP Keys
- Certificates

---

## Project Structure

```text
SafeCommit/
│
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml
├── README.md
│
└── src/
    └── safecommit/
        ├── __init__.py
        ├── cli.py
        ├── scanner.py
        ├── patterns.py
        └── utils.py
```

---

## Contributing

Contributions, bug reports, feature requests, and improvements are welcome.

Please open an issue before submitting major changes.

---

## License

This project is licensed under the MIT License.

---

## Author

**Sushant Kumar Kushwaha**

GitHub: https://github.com/sushantkr1187
