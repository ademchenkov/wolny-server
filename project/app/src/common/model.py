import uuid

from tortoise.models import Model
from tortoise import fields


class MyModel(Model):
	id = fields.UUIDField(pk=True, default=uuid.uuid4)
	created_at = fields.DatetimeField(null=False, auto_now_add=True)
	updated_at = fields.DatetimeField(auto_now=True)
	is_deleted = fields.BooleanField(null=False, default=False)

	class Meta:
		abstract = True

	@classmethod
	async def create_instance(cls, **kwargs):
		return await cls.create(**kwargs)

	@classmethod
	async def get_instance(cls, id):
		return await cls.get(id=id)

	@classmethod
	async def update_instance(cls, id, **kwargs):
		await cls.filter(id=id).update(is_deleted=True)

	@classmethod
	async def delete_instance(cls, id):
		await cls.filter(id=id).update()
		return await cls.get(id=id)

	@classmethod
	async def get_all_instances(cls):
		return await cls.all()