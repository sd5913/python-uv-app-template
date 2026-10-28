#!/usr/bin/env bash
set -euo pipefail
uv sync --locked --group build
uv run --locked python -m unittest discover -s tests
uv run --locked python main.py --smoke-test
