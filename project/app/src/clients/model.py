from tortoise.models import Model
from tortoise import fields


class Client(Model):
	id = fields.CharField(pk=True, max_length=8)
	name = fields.CharField(null=False, max_length=30)
	surname = fields.CharField(null=False, max_length=30)
	phone = fields.CharField(null=False, max_length=30)
	email = fields.CharField

	class Meta:
		table = "clients"