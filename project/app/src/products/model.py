from tortoise import fields

from project.app.src.common.model import MyModel


class Product(MyModel):
	is_active = fields.BooleanField(null=False)
	product_data = fields.JSONField(null=False)

	class Meta:
		table = "products"
