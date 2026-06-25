uv venv
source .venv/bin/activate
uv init

uv run uvicorn app.main:app --reload

uv add alembic
