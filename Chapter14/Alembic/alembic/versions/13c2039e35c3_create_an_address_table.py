"""create an address table

Revision ID: 13c2039e35c3
Revises: 
Create Date: 2023-12-20 16:32:02.034169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13c2039e35c3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('address', sa.Column('id', sa.Integer, primary_key = True), sa.Column('address', sa.String(50), nullable = False),sa.Column('city', sa.String(50), nullable = False), sa.Column('state', sa.String(50), nullable = False))

def downgrade() -> None:
    op.drop_table('address')