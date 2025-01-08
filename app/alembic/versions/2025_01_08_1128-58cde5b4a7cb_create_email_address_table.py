"""create email_address table

Revision ID: 58cde5b4a7cb
Revises: 
Create Date: 2025-01-08 11:28:52.413675

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "58cde5b4a7cb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "addresses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email_address", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_addresses_email_address"),
        "addresses",
        ["email_address"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_addresses_email_address"), table_name="addresses")
    op.drop_table("addresses")
