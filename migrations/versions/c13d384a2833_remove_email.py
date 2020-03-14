"""remove email

Revision ID: c13d384a2833
Revises: 95c6a83db046
Create Date: 2020-03-14 16:45:44.737627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c13d384a2833'
down_revision = '95c6a83db046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.TEXT(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
