"""test

Revision ID: d57f3787f701
Revises: 370b1db8ad89
Create Date: 2025-01-02 13:14:29.327930

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd57f3787f701'
down_revision: Union[str, None] = '370b1db8ad89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
