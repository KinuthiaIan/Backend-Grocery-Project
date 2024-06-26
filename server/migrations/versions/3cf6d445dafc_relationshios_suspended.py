"""relationshios suspended

Revision ID: 3cf6d445dafc
Revises: b5aa09b7d98e
Create Date: 2024-04-21 23:21:10.612277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cf6d445dafc'
down_revision = 'b5aa09b7d98e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_products_users_id_users', 'products', type_='foreignkey')
    op.drop_column('products', 'users_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('users_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key('fk_products_users_id_users', 'products', 'users', ['users_id'], ['id'])
    # ### end Alembic commands ###
