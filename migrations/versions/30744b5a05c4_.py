"""empty message

Revision ID: 30744b5a05c4
Revises: 576658b13cb6
Create Date: 2023-08-18 22:46:05.152881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30744b5a05c4'
down_revision = '576658b13cb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_pembinaan', schema=None) as batch_op:
        batch_op.drop_constraint('data_pembinaan_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'detail_siswa', ['siswa_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_pembinaan', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('data_pembinaan_ibfk_1', 'detail_siswa', ['siswa_id'], ['id'])

    # ### end Alembic commands ###
