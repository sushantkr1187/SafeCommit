"""
safecommit.scanner

Search Engine for SafeCommit.

Responsibilities:
- Traverse directories recursively.
- Ignore unwanted folders.
- Read supported text files.
- Match file contents against regex patterns.
- Collect findings.
- Return scan results.

Author: Sushant Kumar Kushwaha
"""

from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
from safecommit.patterns import PATTERNS
from safecommit.utils import (is_supported_file,should_ignore,read_text_file)

@dataclass(slots=True)
class Finding:
    file: Path
    line: int
    severity: str
    pattern: str
    match: str

    def __str__(self) -> str:
        return (
            f"File      : {self.file}\n"
            f"Line      : {self.line}\n"
            f"Severity  : {self.severity}\n"
            f"Pattern   : {self.pattern}\n"
            f"Match     : {self.match}"
        )

class ScanDirectory:
    """
    Main Search Engine.
    """
    MAX_FILE_SIZE=20*1024*1024 # 20 MB
    def __init__(self,root:Path):
        self.root=root
        self.files_scanned=0
        self.files_skipped=0
        self.findings: list[Finding]=[]
    def scan(self) -> list[Finding]:
        """
        Entry Point.
        """
        self._walk_directory()
        return self.findings
    def _walk_directory(self) -> None:
        """
        Traverse every file recursively.
        """
        for file in self.root.rglob('*'):
            if not file.is_file(): continue
            if should_ignore(file): self.files_skipped+=1; continue
            if not is_supported_file(file): self.files_skipped+=1; continue
            if file.stat().st_size>self.MAX_FILE_SIZE: self.files_skipped+=1; continue
            self._scan_file(file)
    def _scan_file(self,file:Path) -> None:
        """
        Scan one file.
        """
        self.files_scanned+=1
        text=read_text_file(file)
        if text is None: return
        self._detect_patterns(file=file,text=text)
    def _detect_patterns(self,file:Path,text:str) -> None:
        """
        Compare file contents against every pattern.
        """
        lines=text.splitlines()
        for l_no,line in enumerate(lines,start=1):
            for pattern in PATTERNS:
                matches=pattern["regex"].finditer(line)
                for match in matches:
                    finding=Finding(file=file,line=l_no,severity=pattern['severity'],pattern=pattern['name'],match=match.group(0))
                    self.findings.append(finding)