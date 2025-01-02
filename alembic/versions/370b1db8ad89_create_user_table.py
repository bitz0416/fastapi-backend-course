"""create user table

Revision ID: 370b1db8ad89
Revises: ddc3a8248210
Create Date: 2025-01-02 13:13:30.488766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '370b1db8ad89'
down_revision: Union[str, None] = 'ddc3a8248210'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
