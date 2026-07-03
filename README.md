uv venv
source .venv/bin/activate
uv init

uv run uvicorn app.main:app --reload

uv add alembic
uv run alembic upgrade head(run)
uv run alembic upgrade head --sql
uv run alembic current(current version)
