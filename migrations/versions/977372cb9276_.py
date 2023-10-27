"""empty message

Revision ID: 977372cb9276
Revises: 
Create Date: 2023-10-23 12:06:54.660665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '977372cb9276'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('street', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('color', sa.String(length=20), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('product')
    op.drop_table('address')
    # ### end Alembic commands ###