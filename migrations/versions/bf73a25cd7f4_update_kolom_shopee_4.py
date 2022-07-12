"""update kolom shopee 4

Revision ID: bf73a25cd7f4
Revises: dcdc2d1e5a1c
Create Date: 2022-07-07 09:05:37.448438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf73a25cd7f4'
down_revision = 'dcdc2d1e5a1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tabel_shopee_tokped', sa.Column('bulan_pelaporan', sa.Integer(), nullable=True))
    op.add_column('tabel_shopee_tokped', sa.Column('tahun_pelaporan', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tabel_shopee_tokped', 'tahun_pelaporan')
    op.drop_column('tabel_shopee_tokped', 'bulan_pelaporan')
    # ### end Alembic commands ###
