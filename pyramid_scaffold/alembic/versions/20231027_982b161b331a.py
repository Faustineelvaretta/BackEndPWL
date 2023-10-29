"""init

Revision ID: 982b161b331a
Revises: 91e0e639b8a1
Create Date: 2023-10-27 12:16:02.004785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '982b161b331a'
down_revision = '91e0e639b8a1'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_models'))
    )
    op.create_index('my_index', 'models', ['name'], unique=True, mysql_length=255)
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_products'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )
    op.create_table('shopping_carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_shopping_carts_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_shopping_carts'))
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_transactions_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_transactions'))
    )
    op.create_table('shopping_cart_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['shopping_carts.id'], name=op.f('fk_shopping_cart_items_cart_id_shopping_carts')),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_shopping_cart_items_product_id_products')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_shopping_cart_items'))
    )
    op.create_table('transaction_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_transaction_details_product_id_products')),
    sa.ForeignKeyConstraint(['transaction_id'], ['transactions.id'], name=op.f('fk_transaction_details_transaction_id_transactions')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_transaction_details'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction_details')
    op.drop_table('shopping_cart_items')
    op.drop_table('transactions')
    op.drop_table('shopping_carts')
    op.drop_table('users')
    op.drop_table('products')
    op.drop_index('my_index', table_name='models', mysql_length=255)
    op.drop_table('models')
    # ### end Alembic commands ###
