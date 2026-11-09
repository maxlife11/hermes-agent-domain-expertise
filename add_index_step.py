#!/usr/bin/env python3
"""Deprecated mutation helper. Validate the canonical sources without rewriting them."""
import subprocess
import sys
from pathlib import Path

if __name__ == '__main__':
    print('Deprecated: edit INDEX.md and phase sources explicitly; validating without mutation.', flush=True)
    raise SystemExit(subprocess.call([sys.executable, str(Path(__file__).parent / 'scripts/build_report.py'), '--check']))
