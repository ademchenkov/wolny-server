from tortoise.models import Model
from tortoise import fields


class Product(Model):
	id = fields.IntField(pk=True)
	product_data = fields.JSONField(null=False)