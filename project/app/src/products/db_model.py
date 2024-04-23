from tortoise import fields

from project.app.src.common.db_model import DBModel


class ProductImage(DBModel):
	product = fields.ForeignKeyField("wolny.Product", related_name="images", null=False)
	url = fields.CharField(null=False, max_length=300)

	class Meta:
		table = "product_images"


class ProductDescription(DBModel):
	product = fields.ForeignKeyField("wolny.Product", related_name="descriptions", null=False)
	title = fields.CharField(null=False, max_length=20)
	text = fields.CharField(null=False, max_length=300)

	class Meta:
		table = "product_descriptions"
		unique_together = ("product", "title")


class ProductAdvantage(DBModel):
	product = fields.ForeignKeyField("wolny.Product", related_name="advantages", null=False)
	text = fields.CharField(null=False, max_length=15)

	class Meta:
		table = "product_advantages"
		unique_together = ("product", "text")


class Product(DBModel):
	name = fields.CharField(null=False, max_length=60, unique=True)

	class Meta:
		table = "products"
