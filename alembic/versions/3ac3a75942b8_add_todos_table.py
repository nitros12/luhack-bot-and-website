"""Add todos table

Revision ID: 3ac3a75942b8
Revises: 12e1b92b897f
Create Date: 2019-09-10 23:07:46.553853

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '3ac3a75942b8'
down_revision = '12e1b92b897f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assigned', sa.BigInteger(), nullable=True),
    sa.Column('started', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('cancelled', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('completed', sa.DateTime(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    # ### end Alembic commands ###
