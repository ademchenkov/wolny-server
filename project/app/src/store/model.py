from enum import Enum

from tortoise.models import Model
from tortoise import fields


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


class ProductItem(Model):
	item_id = fields.IntField(pk=True)
	product_id = fields.ForeignKeyField("prices.Product", related_name="id", null=False)
	size = fields.CharEnumField(ProductItemSize, null=False)
	status = fields.CharEnumField(ProductItemState, null=False)
