from tortoise import fields

from project.app.src.common.model import MyModel


class Price(MyModel):
	product = fields.ForeignKeyField("wolny.Product", related_name="prices", null=False)
	from_datetime = fields.DatetimeField(null=False)
	full_price = fields.FloatField(null=False)
	sale_price = fields.FloatField

	class Meta:
		table = "prices"
