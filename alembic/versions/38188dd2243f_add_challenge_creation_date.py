"""Add challenge creation_date

Revision ID: 38188dd2243f
Revises: b0df6f4097b7
Create Date: 2020-09-19 06:34:59.966877

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '38188dd2243f'
down_revision = 'b0df6f4097b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('challenges', sa.Column('creation_date', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('challenges', 'creation_date')
    # ### end Alembic commands ###
