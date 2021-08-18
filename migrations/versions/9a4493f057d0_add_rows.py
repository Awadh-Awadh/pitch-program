"""add rows

Revision ID: 9a4493f057d0
Revises: cc3444698bf1
Create Date: 2021-08-17 21:50:01.622413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a4493f057d0'
down_revision = 'cc3444698bf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('upvote', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('downvote', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'downvote')
    op.drop_column('pitches', 'upvote')
    # ### end Alembic commands ###