import uuid
from typing import Any
from typing import Optional
from typing import Type

from tortoise import BaseDBAsyncClient
from tortoise.models import MODEL
from tortoise.models import Model
from tortoise import fields


class DBModel(Model):
	id = fields.CharField(pk=True, max_length=36)
	created_at = fields.DatetimeField(null=False, auto_now_add=True)
	updated_at = fields.DatetimeField(auto_now=True)
	is_deleted = fields.BooleanField(null=False, default=False)

	class Meta:
		abstract = True

	@classmethod
	async def create_with_id(
			cls: Type[MODEL], using_db: Optional[BaseDBAsyncClient] = None, **kwargs: Any
	) -> MODEL:
		new_id = str(uuid.uuid4())
		instance = cls(id=new_id, **kwargs)
		instance._saved_in_db = False
		db = using_db or cls._choose_db(True)
		await instance.save(using_db=db, force_create=True)
		return instance