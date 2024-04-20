from enum import Enum

from tortoise import fields

from project.app.src.common.model import MyModel


class ProductItemSize(str, Enum):
	XS = "XS"
	S = "S"
	M = "M"
	L = "L"


class ProductItemState(str, Enum):
	UNAVAILABLE = "unavailable"
	IN_STOCK = "in stock"
	PAID = "paid"
	READY_TO_DELIVERY = "ready to delivery"
	DELIVERED = "delivered"


class ProductItem(MyModel):
	product = fields.ForeignKeyField("wolny.Product", related_name="productItems", null=False)
	size = fields.CharEnumField(ProductItemSize, null=False)
	status = fields.CharEnumField(ProductItemState, null=False)

	class Meta:
		table = "product_items"
