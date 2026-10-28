# Little Signals

Use Python 3.13 and uv. Run `uv sync --locked --group build`,
`uv run --locked python -m unittest discover -s tests`, and
`uv run --locked python main.py --smoke-test` after changes. Use a graphical
machine to check the real interaction. `build/`, `dist/`, `.venv/`, secrets and
credentials do not belong in Git. Explain behavior and test steps in each PR.
