"""add column for relationship

Revision ID: 29b69fb24513
Revises: dd3b2db12cd1
Create Date: 2021-08-19 15:09:33.391352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29b69fb24513'
down_revision = 'dd3b2db12cd1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    # ### end Alembic commands ###
