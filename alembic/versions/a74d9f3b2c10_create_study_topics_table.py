"""create study_topics table

Revision ID: a74d9f3b2c10
Revises: f0a8f1a2c9b4
Create Date: 2026-07-11 00:00:00.000000

"""
from typing import Sequence
from typing import Union

from alembic import op
import sqlalchemy as sa


revision: str = "a74d9f3b2c10"
down_revision: Union[str, Sequence[str], None] = "f0a8f1a2c9b4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "study_topics",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("subject", sa.String(length=120), nullable=True),
        sa.Column("target_date", sa.Date(), nullable=True),
        sa.Column("is_completed", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_study_topics_subject"),
        "study_topics",
        ["subject"],
        unique=False,
    )
    op.create_index(
        op.f("ix_study_topics_user_id"),
        "study_topics",
        ["user_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_study_topics_user_id"),
        table_name="study_topics",
    )
    op.drop_index(
        op.f("ix_study_topics_subject"),
        table_name="study_topics",
    )
    op.drop_table("study_topics")
