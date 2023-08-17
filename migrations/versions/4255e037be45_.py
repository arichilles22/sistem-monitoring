"""empty message

Revision ID: 4255e037be45
Revises: 06066e407bc8
Create Date: 2023-08-17 02:31:33.070450

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4255e037be45'
down_revision = '06066e407bc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_pelanggaran', schema=None) as batch_op:
        batch_op.add_column(sa.Column('guru_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'detail_guru', ['guru_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
        batch_op.drop_column('pelapor')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_pelanggaran', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pelapor', mysql.VARCHAR(length=128), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('guru_id')

    # ### end Alembic commands ###
