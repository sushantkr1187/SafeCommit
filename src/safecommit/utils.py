"""
safecommit.utils

Utility functions used throughout SafeCommit.

Author: Sushant Kumar Kushwaha
"""

from __future__ import annotations
from pathlib import Path

SUPPORTED_EXTENSIONS = {".py",".js",".ts",".jsx",".tsx",".java",".c",".cpp",".cc",".cs",".go",".rs",".php",".rb",".swift",".kt",".kts",".scala",".sql",".html",".css",".scss",".sass",".json",".yaml",".yml",".toml",".ini",".cfg",".env",".txt",".md",".xml",".properties",".sh",".bat",".ps1"}

SUPPORTED_FILENAMES = {".env",".env.local",".env.development",".env.production",".env.test",".gitignore","Dockerfile","docker-compose.yml","docker-compose.yaml","Makefile","README","README.md"}

IGNORED_DIRECTORIES = {".git",".idea",".vscode","__pycache__","venv",".venv","env","node_modules","dist","build","target",".pytest_cache",".mypy_cache"}

def should_ignore(path: Path) -> bool:
    """
    Return True if the file resides inside an ignored directory.
    """
    return any(part in IGNORED_DIRECTORIES for part in path.parts)

def is_supported_file(path: Path) -> bool:
    """
    Check whether a file should be scanned.
    """
    return (path.suffix.lower() in SUPPORTED_EXTENSIONS or path.name in SUPPORTED_FILENAMES)

def read_text_file(path: Path) -> str | None:
    """
    Safely read a text file.

    Returns
    -------
    str
        File contents.

    None
        If the file cannot be read.
    """
    try:
        return path.read_text(encoding="utf-8",errors="ignore")
    except (OSError, UnicodeDecodeError):
        return None

def relative_path(root: Path, file: Path) -> Path:
    """
    Return file path relative to the scan root.
    """
    try: return file.relative_to(root)
    except ValueError: return file

def plural(word: str, count: int) -> str:
    """
    Basic pluralization helper.

    Example
    -------
    1 file
    2 files
    """
    return word if count == 1 else f"{word}s"

def is_hidden(path: Path) -> bool:
    """
    Return True if the file or directory is hidden.
    """
    return any(part.startswith(".") for part in path.parts)