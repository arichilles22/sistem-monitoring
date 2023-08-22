"""empty message

Revision ID: 83ce577adf07
Revises: 2bd9e6f60f5b
Create Date: 2023-08-22 13:40:05.856098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83ce577adf07'
down_revision = '2bd9e6f60f5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_pembinaan', schema=None) as batch_op:
        batch_op.drop_constraint('data_pembinaan_ibfk_4', type_='foreignkey')
        batch_op.create_foreign_key(None, 'data_pelanggaran', ['pelanggaran_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_pembinaan', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('data_pembinaan_ibfk_4', 'data_pelanggaran', ['pelanggaran_id'], ['id'])

    # ### end Alembic commands ###
