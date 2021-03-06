"""migrate3

Revision ID: 4fc9b67de55e
Revises: 55e357815b2d
Create Date: 2022-07-05 10:48:34.013703

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4fc9b67de55e'
down_revision = '55e357815b2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_admin')
    op.drop_column('user', 'is_super_admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_super_admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('is_admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
