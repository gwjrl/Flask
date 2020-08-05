"""empty message

Revision ID: 6379a20b2851
Revises: 
Create Date: 2020-08-04 22:27:37.952229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6379a20b2851'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('icon', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
