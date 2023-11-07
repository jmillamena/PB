"""creates relationships

Revision ID: c8141a7ce73f
Revises: e4a61c246e48
Create Date: 2023-10-16 06:19:58.104887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8141a7ce73f'
down_revision = 'e4a61c246e48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('house_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('wand_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('pet_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_students_pet_id_pets'), 'pets', ['pet_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_students_wand_id_wands'), 'wands', ['wand_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_students_house_id_houses'), 'houses', ['house_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_students_house_id_houses'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_students_wand_id_wands'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_students_pet_id_pets'), type_='foreignkey')
        batch_op.drop_column('pet_id')
        batch_op.drop_column('wand_id')
        batch_op.drop_column('house_id')

    # ### end Alembic commands ###
