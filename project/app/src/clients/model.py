from tortoise import fields

from project.app.src.common.model import MyModel


class Client(MyModel):
	name = fields.CharField(null=False, max_length=30)
	surname = fields.CharField(null=False, max_length=30)
	phone = fields.CharField(null=False, max_length=30)
	email = fields.CharField

	class Meta:
		table = "clients"
