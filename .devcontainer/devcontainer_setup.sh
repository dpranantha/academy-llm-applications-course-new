curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.11.6
uv python use 3.11.6

uv sync
uv run python -m ipykernel install --user --name=venv