"""update tabel upload excel 1

Revision ID: ecffe7efe646
Revises: bf73a25cd7f4
Create Date: 2022-07-07 11:56:33.999868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecffe7efe646'
down_revision = 'bf73a25cd7f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tabel_upload_excel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama_file', sa.String(length=100), nullable=True),
    sa.Column('bulan_pelaporan', sa.Integer(), nullable=True),
    sa.Column('tahun_pelaporan', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.String(length=100), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('status_aktif', sa.String(length=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tabel_upload_excel')
    # ### end Alembic commands ###
