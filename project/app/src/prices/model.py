from tortoise.models import Model
from tortoise import fields


class Price(Model):
	id = fields.IntField(pk=True)
	product = fields.ForeignKeyField("wolny.Product", related_name="prices", null=False)
	from_datetime = fields.DatetimeField(null=False)
	full_price = fields.FloatField(null=False)
	sale_price = fields.FloatField

	class Meta:
		table = "prices"