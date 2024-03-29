"""empty message

Revision ID: af64f2d85879
Revises: 9100786d40af
Create Date: 2021-10-11 15:40:41.505732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af64f2d85879'
down_revision = '9100786d40af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('post', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_index('ix_user_username', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('post', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('comment', 'name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###
