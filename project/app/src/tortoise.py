import os


TORTOISE_ORM = {
	"connections": {"default": os.environ.get("DATABASE_URL")},
	"apps": {
		"wolny": {
			"models": [
				"project.app.src.clients.db_model",
				"project.app.src.orders.db_model",
				"project.app.src.prices.db_model",
				"project.app.src.products.db_model",
				"project.app.src.store.db_model"
			],
			"default_connection": "default",
		},
	},
}