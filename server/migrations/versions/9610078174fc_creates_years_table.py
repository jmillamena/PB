"""creates years table

Revision ID: 9610078174fc
Revises: c8141a7ce73f
Create Date: 2023-10-16 07:55:01.677431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9610078174fc'
down_revision = 'c8141a7ce73f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('years',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('year_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_students_year_id_years'), 'years', ['year_id'], ['id'])

    with op.batch_alter_table('wands', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wands', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_students_year_id_years'), type_='foreignkey')
        batch_op.drop_column('year_id')

    op.drop_table('years')
    # ### end Alembic commands ###