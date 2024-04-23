from tortoise import fields

from project.app.src.common.db_model import DBModel


class Price(DBModel):
	product = fields.ForeignKeyField("wolny.Product", related_name="prices", null=False)
	from_datetime = fields.DatetimeField(null=False)
	full_price = fields.FloatField(null=False)
	sale_price = fields.FloatField
	has_sale = fields.BooleanField(null=False, default=False)

	class Meta:
		table = "prices"
