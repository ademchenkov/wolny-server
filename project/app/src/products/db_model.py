from tortoise import fields

from project.app.src.common.db_model import DBModel


class ProductImageDb(DBModel):
	product = fields.ForeignKeyField("wolny.ProductDb", related_name="images", null=False)
	url = fields.CharField(null=False, max_length=300)

	class Meta:
		table = "product_images"


class ProductDescriptionDb(DBModel):
	product = fields.ForeignKeyField("wolny.ProductDb", related_name="descriptions", null=False)
	title = fields.CharField(null=False, max_length=20)
	text = fields.CharField(null=False, max_length=300)

	class Meta:
		table = "product_descriptions"
		unique_together = ("product", "title")


class ProductAdvantageDb(DBModel):
	product = fields.ForeignKeyField("wolny.ProductDb", related_name="advantages", null=False)
	text = fields.CharField(null=False, max_length=15)

	class Meta:
		table = "product_advantages"
		unique_together = ("product", "text")


class ProductDb(DBModel):
	name = fields.CharField(null=False, max_length=60)

	class Meta:
		table = "products"
