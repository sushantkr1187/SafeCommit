"""
Command Line Interface for SafeCommit.
"""

from __future__ import annotations
from pathlib import Path
import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from safecommit import __version__
from safecommit.scanner import ScanDirectory

console = Console()
app = typer.Typer(name="safecommit",help="Scan projects for exposed secrets and sensitive information.",no_args_is_help=True,add_completion=False)

@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context,version: bool = typer.Option(False,"-v","--version",help="Show the installed version and exit.",is_eager=True)) -> None:
    """
    Global CLI options.
    """
    if version: console.print(f"SafeCommit v{__version__}"); raise typer.Exit()
    if ctx.invoked_subcommand is None: raise typer.Exit()

@app.command()
def scan(path: Path = typer.Argument(Path.cwd(),exists=True,file_okay=False,dir_okay=True,readable=True,resolve_path=True,help="Directory to scan.")) -> None:
    """
    Scan a project for exposed secrets.
    """
    console.print(f"\nScanning: [cyan]{path}[/cyan]\n")
    scanner = ScanDirectory(path)
    findings = scanner.scan()
    if not findings:
        console.print("[bold green]✓ No sensitive information detected.[/bold green]")
        raise typer.Exit(code=0)
    console.print(f"[bold red]Found {len(findings)} potential issue(s).[/bold red]\n")
    for finding in findings:
        severity_color = {"CRITICAL": "bold red","HIGH": "red","MEDIUM": "yellow","LOW": "green",}.get(finding.severity, "white")

        body = Text()
        body.append(f"File      : {finding.file}\n", style="cyan")
        body.append(f"Line      : {finding.line}\n", style="magenta")
        body.append(f"Severity  : {finding.severity}\n", style=severity_color)
        body.append(f"Pattern   : {finding.pattern}\n", style="yellow")
        body.append(f"Match     : {finding.match}", style="bold")

        console.print(Panel(body,title=f"[{severity_color}]Secret Detected[/]",border_style=severity_color))
    raise typer.Exit(code=1)

@app.command()
def version() -> None:
    """
    Show the installed SafeCommit version.
    """
    console.print(f"SafeCommit v{__version__}")

def main() -> None:
    """
    Package entry point.
    """
    app()

if __name__ == "__main__":
    main()