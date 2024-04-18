from enum import Enum

from tortoise.models import Model
from tortoise import fields


class OrderPlatform(str, Enum):
	IOS = "iOS"
	TELEGRAM = "Telegram"


class Order(Model):
	id = fields.CharField(pk=True, max_length=8)
	client = fields.ForeignKeyField("wolny.Client", related_name="orders", null=False)
	order_platform = fields.CharEnumField(OrderPlatform)
	payment_type = fields.CharField  # добавить enum для того, чтобы понимать канал оплаты
	delivery_address = fields.CharField

	class Meta:
		table = "orders"


class OrderItems(Model):
	order = fields.ForeignKeyField("wolny.Order", related_name="orderItems")
	item = fields.ForeignKeyField("wolny.ProductItem", related_name="orderItems")
	paid_price = fields.FloatField

	class Meta:
		unique_together = ("order_id", "item_id")
		primary_key = ("order_id", "item_id")
		table = "order_items"