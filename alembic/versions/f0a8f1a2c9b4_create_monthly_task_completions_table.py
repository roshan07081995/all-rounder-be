"""create monthly_task_completions table

Revision ID: f0a8f1a2c9b4
Revises: c52f9dc3daa1
Create Date: 2026-07-04 20:15:00.000000

"""
from typing import Sequence
from typing import Union

from alembic import op
import sqlalchemy as sa


revision: str = "f0a8f1a2c9b4"
down_revision: Union[str, Sequence[str], None] = "c52f9dc3daa1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "monthly_task_completions",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("task_id", sa.UUID(), nullable=False),
        sa.Column("completion_date", sa.Date(), nullable=False),
        sa.Column(
            "is_completed",
            sa.Boolean(),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["daily_tasks.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "user_id",
            "task_id",
            "completion_date",
            name="uq_monthly_task_completion_user_task_date",
        ),
    )
    op.create_index(
        op.f("ix_monthly_task_completions_completion_date"),
        "monthly_task_completions",
        ["completion_date"],
        unique=False,
    )
    op.create_index(
        op.f("ix_monthly_task_completions_task_id"),
        "monthly_task_completions",
        ["task_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_monthly_task_completions_user_id"),
        "monthly_task_completions",
        ["user_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_monthly_task_completions_user_id"),
        table_name="monthly_task_completions",
    )
    op.drop_index(
        op.f("ix_monthly_task_completions_task_id"),
        table_name="monthly_task_completions",
    )
    op.drop_index(
        op.f("ix_monthly_task_completions_completion_date"),
        table_name="monthly_task_completions",
    )
    op.drop_table("monthly_task_completions")
