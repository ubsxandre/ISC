"""update tabel upload excel 4

Revision ID: 5b0e2fcfa1dc
Revises: 3673ef642007
Create Date: 2022-07-07 13:33:11.391784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b0e2fcfa1dc'
down_revision = '3673ef642007'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tabel_shopee_tokped',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('waktu_pesanan_dibuat', sa.DateTime(), nullable=True),
    sa.Column('status_pesanan', sa.String(length=100), nullable=True),
    sa.Column('nama_produk', sa.String(length=100), nullable=True),
    sa.Column('nomer_referensi_sku', sa.String(length=100), nullable=True),
    sa.Column('harga_awal', sa.Float(precision=15, asdecimal=2), nullable=True),
    sa.Column('jumlah', sa.Float(precision=6, asdecimal=2), nullable=True),
    sa.Column('username_pembeli', sa.String(length=100), nullable=True),
    sa.Column('kota_kabupaten', sa.String(length=100), nullable=True),
    sa.Column('provinsi', sa.String(length=100), nullable=True),
    sa.Column('olshop', sa.String(length=100), nullable=True),
    sa.Column('bulan_pelaporan', sa.String(length=2), nullable=True),
    sa.Column('tahun_pelaporan', sa.String(length=4), nullable=True),
    sa.Column('created_by', sa.String(length=100), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('status_aktif', sa.String(length=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tabel_upload_excel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file', sa.String(length=100), nullable=True),
    sa.Column('olshop', sa.String(length=100), nullable=True),
    sa.Column('bulan_pelaporan', sa.String(length=2), nullable=True),
    sa.Column('tahun_pelaporan', sa.String(length=4), nullable=True),
    sa.Column('created_by', sa.String(length=100), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('status_aktif', sa.String(length=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tabel_upload_excel')
    op.drop_table('tabel_shopee_tokped')
    # ### end Alembic commands ###
