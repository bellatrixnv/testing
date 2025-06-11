# Speed Test CLI Tool

This repository provides a simple command line speed test application for Linux. It uses the [`speedtest-cli`](https://github.com/sivel/speedtest-cli) library to measure your internet connection and the [`rich`](https://github.com/Textualize/rich) package for colorful interactive output.

## Requirements

- Python 3.7+
- `speedtest-cli` and `rich` packages (`pip install speedtest-cli rich`)

## Usage

Run the script directly:

```bash
python speedtest_cli.py
```

The tool will select the best server, run download and upload tests, and display the results in a formatted table.
