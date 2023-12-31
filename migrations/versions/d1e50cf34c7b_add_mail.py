"""add Mail

Revision ID: d1e50cf34c7b
Revises: ad6e221931ff
Create Date: 2023-10-30 23:47:25.321365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1e50cf34c7b'
down_revision = 'ad6e221931ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('to_email', sa.String(length=64), nullable=True),
    sa.Column('mail_topic', sa.String(length=50), nullable=True),
    sa.Column('mail_message', sa.String(length=800), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('mail', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_mail_mail_topic'), ['mail_topic'], unique=False)
        batch_op.create_index(batch_op.f('ix_mail_to_email'), ['to_email'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mail', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_mail_to_email'))
        batch_op.drop_index(batch_op.f('ix_mail_mail_topic'))

    op.drop_table('mail')
    # ### end Alembic commands ###
