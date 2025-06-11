#!/usr/bin/env python3
"""Simple CLI Internet speed test using rich for output."""

import sys

try:
    from rich.console import Console
    from rich.table import Table
    from rich.progress import Progress
    import speedtest
except ImportError as exc:
    sys.stderr.write(
        "Missing dependencies. Install with 'pip install speedtest-cli rich'\n"
    )
    raise


def run_speedtest():
    console = Console()
    st = speedtest.Speedtest()

    with Progress(console=console, transient=True) as progress:
        task = progress.add_task("Selecting server...", total=3)
        st.get_servers()
        progress.advance(task)

        st.get_best_server()
        progress.update(task, description="Testing download speed...")
        st.download()
        progress.advance(task)

        progress.update(task, description="Testing upload speed...")
        st.upload()
        progress.advance(task)

    results = st.results.dict()

    table = Table(title="Speed Test Results", show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="dim")
    table.add_column("Value", justify="right")

    table.add_row("Ping", f"{results['ping']:.2f} ms")
    table.add_row("Download", f"{results['download'] / 1_000_000:.2f} Mbps")
    table.add_row("Upload", f"{results['upload'] / 1_000_000:.2f} Mbps")
    table.add_row("Server", results['server']['sponsor'])

    console.print(table)


if __name__ == "__main__":
    run_speedtest()
