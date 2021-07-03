"""Create initial page and scrape tables

Revision ID: 326f35ee99e4
Revises: 
Create Date: 2021-07-03 20:56:31.706463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '326f35ee99e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scrape',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('extracted_page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scrape_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['scrape_id'], ['scrape.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('extracted_page')
    op.drop_table('scrape')
    # ### end Alembic commands ###
