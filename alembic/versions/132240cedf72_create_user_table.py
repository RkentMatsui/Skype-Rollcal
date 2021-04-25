"""create user table

Revision ID: 132240cedf72
Revises: 9988922875f1
Create Date: 2021-04-25 10:48:47.351729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '132240cedf72'
down_revision = '9988922875f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skype_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('skype_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
