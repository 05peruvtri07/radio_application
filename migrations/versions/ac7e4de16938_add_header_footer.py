"""add header footer

Revision ID: ac7e4de16938
Revises: d1e50cf34c7b
Create Date: 2023-11-22 05:00:40.478386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac7e4de16938'
down_revision = 'd1e50cf34c7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('header', sa.String(length=300), nullable=True))
        batch_op.add_column(sa.Column('footer', sa.String(length=300), nullable=True))
        batch_op.create_index(batch_op.f('ix_users_footer'), ['footer'], unique=False)
        batch_op.create_index(batch_op.f('ix_users_header'), ['header'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_header'))
        batch_op.drop_index(batch_op.f('ix_users_footer'))
        batch_op.drop_column('footer')
        batch_op.drop_column('header')

    # ### end Alembic commands ###
