import uuid

from tortoise.models import Model
from tortoise import fields


class DBModel(Model):
	id = fields.UUIDField(pk=True, default=uuid.uuid4)
	created_at = fields.DatetimeField(null=False, auto_now_add=True)
	updated_at = fields.DatetimeField(auto_now=True)
	is_deleted = fields.BooleanField(null=False, default=False)

	class Meta:
		abstract = True