"""empty message

Revision ID: 1724d8ca3a7d
Revises: 8sdfa667s72h
Create Date: 2020-03-27 22:25:01.974261

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1724d8ca3a7d'
down_revision = '8sdfa667s72h'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'end',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('statement_timestamp()'))
    op.alter_column('task', 'start',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('statement_timestamp()'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'start',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('statement_timestamp()'))
    op.alter_column('task', 'end',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('statement_timestamp()'))
    # ### end Alembic commands ###
