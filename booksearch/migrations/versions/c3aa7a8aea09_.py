"""empty message

Revision ID: c3aa7a8aea09
Revises: 23e000370669
Create Date: 2022-06-30 17:36:43.971082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3aa7a8aea09'
down_revision = '23e000370669'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('class_nm', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('isbn13', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('history', schema=None) as batch_op:
        batch_op.drop_column('isbn13')
        batch_op.drop_column('class_nm')

    # ### end Alembic commands ###
