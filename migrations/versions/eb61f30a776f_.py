"""empty message

Revision ID: eb61f30a776f
Revises: 521f6090c6a4
Create Date: 2022-09-03 15:42:14.346912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb61f30a776f'
down_revision = '521f6090c6a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resource_to_course', 'description')
    op.drop_column('resource_to_course', 'importance')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resource_to_course', sa.Column('importance', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('resource_to_course', sa.Column('description', sa.VARCHAR(length=140), autoincrement=False, nullable=True))
    # ### end Alembic commands ###