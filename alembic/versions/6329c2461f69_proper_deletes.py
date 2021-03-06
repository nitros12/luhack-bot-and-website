"""proper deletes

Revision ID: 6329c2461f69
Revises: 5f3d583972c9
Create Date: 2019-04-05 00:59:52.295023

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6329c2461f69'
down_revision = '5f3d583972c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('writeups_author_id_fkey', 'writeups', type_='foreignkey')
    op.create_foreign_key(None, 'writeups', 'users', ['author_id'], ['discord_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'writeups', type_='foreignkey')
    op.create_foreign_key('writeups_author_id_fkey', 'writeups', 'users', ['author_id'], ['discord_id'])
    # ### end Alembic commands ###
