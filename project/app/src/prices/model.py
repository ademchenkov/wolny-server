from tortoise.models import Model
from tortoise import fields


class Prices(Model):
	id = fields.IntField(pk=True)
	product_id = fields.ForeignKeyField("prices.Product", related_name="id", null=False)
	from_datetime = fields.DatetimeField(null=False)
	full_price = fields.FloatField(null=False)
	sale_price = fields.FloatField