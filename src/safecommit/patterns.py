"""
safecommit.patterns
~~~~~~~~~~~~~~~~~~~

Regular expression patterns used to detect exposed secrets.

Author: Sushant Kumar Kushwaha
"""

from __future__ import annotations
import re

PATTERNS = [

    # ==========================================================
    # API KEYS
    # ==========================================================

    {
        "name": "OpenAI API Key",
        "severity": "HIGH",
        "regex": re.compile(r"sk-(proj-)?[A-Za-z0-9_-]{20,}")
    },

    {
        "name": "GitHub Personal Access Token",
        "severity": "HIGH",
        "regex": re.compile(r"gh[pousr]_[A-Za-z0-9]{36,255}")
    },

    {
        "name": "AWS Access Key",
        "severity": "HIGH",
        "regex": re.compile(r'(?i)(aws_secret_access_key|aws_secret_key)\s*[:=]\s*["\']?[A-Za-z0-9/+=]{40}["\']?')
    },

    {
        "name": "Google API Key",
        "severity": "HIGH",
        "regex": re.compile(r"AIza[0-9A-Za-z\-_]{35}")
    },

    {
        "name": "Google OAuth Token",
        "severity": "HIGH",
        "regex": re.compile(r"ya29\.[A-Za-z0-9\-_]+")
    },

    {
        "name": "Slack Token",
        "severity": "HIGH",
        "regex": re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")
    },

    {
        "name": "Stripe Secret Key",
        "severity": "HIGH",
        "regex": re.compile(r"sk_(live|test)_[A-Za-z0-9]{24,}")
    },

    {
        "name": "Stripe Restricted Key",
        "severity": "HIGH",
        "regex": re.compile(r"rk_(live|test)_[A-Za-z0-9]{24,}")
    },

    {
        "name": "GitLab Personal Access Token",
        "severity": "HIGH",
        "regex": re.compile(r"glpat-[A-Za-z0-9\-_]{20,}")
    },

    {
        "name": "PyPI API Token",
        "severity": "HIGH",
        "regex": re.compile(r"pypi-[A-Za-zA-Z0-9_-]{50,}")
    },

    {
        "name": "npm Access Token",
        "severity": "HIGH",
        "regex": re.compile(r"npm_[A-Za-z0-9]{36}")
    },

    {
        "name": "Hugging Face Token",
        "severity": "HIGH",
        "regex": re.compile(r"hf_[A-Za-z0-9]{34,}")
    },

    {
        "name": "Anthropic API Key",
        "severity": "HIGH",
        "regex": re.compile(r"sk-ant-[A-Za-z0-9\-_]{20,}")
    },

    {
        "name": "Groq API Key",
        "severity": "HIGH",
        "regex": re.compile(r"gsk_[A-Za-z0-9]{32,}")
    },

    {
        "name": "Twilio API Key",
        "severity": "HIGH",
        "regex": re.compile(r"SK[a-fA-F0-9]{32}")
    },

    {
        "name": "Discord Bot Token",
        "severity": "HIGH",
        "regex": re.compile(r"[MN][A-Za-z\d]{23}\.[\w-]{6}\.[\w-]{27}")
    },

    {
        "name": "Firebase Cloud Messaging Server Key",
        "severity": "HIGH",
        "regex": re.compile(r"AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}")
    },

    {
        "name": "SendGrid API Key",
        "severity": "HIGH",
        "regex": re.compile(r"SG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}")
    },
    {
        "name": "AWS Secret Access Key",
        "severity": "HIGH",
        "regex": re.compile(r"(?i)aws(.{0,20})?(secret|secret_access_key).{0,20}[=:]\s*[\"']?[A-Za-z0-9/+=]{40}[\"']?")
    },

    # ==========================================================
    # DATABASE CONNECTION STRINGS
    # ==========================================================

    {
        "name": "MongoDB URI",
        "severity": "HIGH",
        "regex": re.compile(r"mongodb(\+srv)?://[^\s\"']+")
    },

    {
        "name": "PostgreSQL URI",
        "severity": "HIGH",
        "regex": re.compile(r"postgres(ql)?://[^\s\"']+")
    },

    {
        "name": "MySQL URI",
        "severity": "HIGH",
        "regex": re.compile(r"mysql://[^\s\"']+")
    },

    {
        "name": "Redis URI",
        "severity": "HIGH",
        "regex": re.compile(r"redis://[^\s\"']+")
    },

    # ==========================================================
    # PRIVATE KEYS
    # ==========================================================

    {
        "name": "Private Key",
        "severity": "CRITICAL",
        "regex": re.compile(
            r"-----BEGIN (RSA |EC |DSA )?PRIVATE KEY-----"
        )
    },

    {
        "name": "SSH Private Key",
        "severity": "CRITICAL",
        "regex": re.compile(
            r"-----BEGIN OPENSSH PRIVATE KEY-----"
        )
    },

    {
        "name": "PGP Private Key",
        "severity": "CRITICAL",
        "regex": re.compile(
            r"-----BEGIN PGP PRIVATE KEY BLOCK-----"
        )
    },

    # ==========================================================
    # TOKENS
    # ==========================================================

    {
        "name": "JWT",
        "severity": "MEDIUM",
        "regex": re.compile(
            r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"
        )
    },

    {
        "name": "Bearer Token",
        "severity": "MEDIUM",
        "regex": re.compile(
            r"Bearer\s+[A-Za-z0-9._\-]+"
        )
    },

    # ==========================================================
    # PASSWORDS
    # ==========================================================

    {
        "name": "Hardcoded Password",
        "severity": "MEDIUM",
        "regex": re.compile(
            r'(?i)\b(password|passwd|pwd|db_password|mysql_password|postgres_password)\b\s*[:=]\s*["\'][^"\']{6,}["\']'
        )
    },

    {
        "name": "Hardcoded Secret",
        "severity": "MEDIUM",
        "regex": re.compile(
            r'(?i)\b[a-z0-9_]*(secret|secret_key|client_secret|app_secret|jwt_secret|api_secret)[a-z0-9_]*\b\s*[:=]\s*["\'][^"\']{8,}["\']'
        )
    },

    {
        "name": "Hardcoded API Key Variable",
        "severity": "MEDIUM",
        "regex": re.compile(
            r'(?i)\b[a-z0-9_]*(api[_-]?key|apikey|access[_-]?key|client[_-]?key|public[_-]?key)[a-z0-9_]*\b\s*[:=]\s*["\'][^"\']{8,}["\']'
        )
    },

    {
        "name": "Hardcoded Token Variable",
        "severity": "MEDIUM",
        "regex": re.compile(
            r'(?i)\b[a-z0-9_]*(token|auth_token|access_token|refresh_token|bearer_token|github_token|discord_token|slack_token|jwt_token)[a-z0-9_]*\b\s*[:=]\s*["\'][^"\']{8,}["\']'
        )
    },

    # ==========================================================
    # CLOUD
    # ==========================================================

    {
        "name": "Azure Storage Connection String",
        "severity": "HIGH",
        "regex": re.compile(
            r"DefaultEndpointsProtocol=https;AccountName=.*?;AccountKey=.*?;"
        )
    },

    {
        "name": "Heroku API Key",
        "severity": "HIGH",
        "regex": re.compile(
            r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
        )
    },

    # ==========================================================
    # CERTIFICATES
    # ==========================================================

    {
        "name": "Certificate",
        "severity": "LOW",
        "regex": re.compile(
            r"-----BEGIN CERTIFICATE-----"
        )
    },
]
