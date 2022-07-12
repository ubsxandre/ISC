"""update tabel upload excel 2

Revision ID: ce376715dd10
Revises: ecffe7efe646
Create Date: 2022-07-07 13:14:35.557654

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ce376715dd10'
down_revision = 'ecffe7efe646'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tabel_upload_excel', sa.Column('file', sa.String(length=100), nullable=True))
    op.drop_column('tabel_upload_excel', 'nama_file')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tabel_upload_excel', sa.Column('nama_file', mysql.VARCHAR(length=100), nullable=True))
    op.drop_column('tabel_upload_excel', 'file')
    # ### end Alembic commands ###