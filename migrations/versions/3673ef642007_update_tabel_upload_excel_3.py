"""update tabel upload excel 3

Revision ID: 3673ef642007
Revises: ce376715dd10
Create Date: 2022-07-07 13:23:03.569087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3673ef642007'
down_revision = 'ce376715dd10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tabel_upload_excel', sa.Column('olshop', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tabel_upload_excel', 'olshop')
    # ### end Alembic commands ###
