"""changed study column to non-nullable and without a default value

Revision ID: 3fecb1504204
Revises: 5c2cc09f46c4
Create Date: 2025-01-26 21:52:52.763956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fecb1504204'
down_revision: Union[str, None] = '5c2cc09f46c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courses', 'study',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courses', 'study',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
