from enum import Enum

from tortoise.models import Model
from tortoise import fields


class OrderPlatform(str, Enum):
	IOS = "iOS"
	TELEGRAM = "Telegram"


class Order(Model):
	id = fields.CharField(pk=True, max_length=8)
	client_id = fields.ForeignKeyField("clients.Client", related_name="id", null=False)
	order_platform = fields.CharEnumField(OrderPlatform)
	payment_type = fields.CharField  # добавить enum для того, чтобы понимать канал оплаты
	delivery_address = fields.CharField


class OrderItems(Model):
	order_id = fields.ForeignKeyField("orders.Order", related_name="id")
	item_id = fields.ForeignKeyField("store.ProductItem", related_name="item_id")
	paid_price = fields.FloatField

	class Meta:
		unique_together = ("order_id", "item_id")
		primary_key = ("order_id", "item_id")