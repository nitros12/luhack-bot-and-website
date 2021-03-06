"""Add creation and edit dates to writeups

Revision ID: da14a852b606
Revises: 98b885be8d35
Create Date: 2019-04-05 00:40:56.569245

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "da14a852b606"
down_revision = "98b885be8d35"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "writeups",
        sa.Column(
            "creation_date",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.add_column(
        "writeups",
        sa.Column(
            "edit_date", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("writeups", "edit_date")
    op.drop_column("writeups", "creation_date")
    # ### end Alembic commands ###
