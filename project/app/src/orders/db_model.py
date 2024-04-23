from enum import Enum

from tortoise import fields

from project.app.src.common.db_model import DBModel


class OrderPlatform(str, Enum):
	IOS = "iOS"
	TELEGRAM = "Telegram"


class Order(DBModel):
	client = fields.ForeignKeyField("wolny.Client", related_name="orders", null=False)
	order_platform = fields.CharEnumField(OrderPlatform)
	payment_type = fields.CharField  # добавить enum для того, чтобы понимать канал оплаты
	delivery_address = fields.CharField

	class Meta:
		table = "orders"


class OrderItems(DBModel):
	order = fields.ForeignKeyField("wolny.Order", related_name="orderItems")
	item = fields.ForeignKeyField("wolny.ProductItem", related_name="orderItems")
	paid_price = fields.FloatField

	class Meta:
		unique_together = ("order_id", "item_id")
		table = "order_items"
