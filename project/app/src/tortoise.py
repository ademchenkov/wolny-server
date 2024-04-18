import os


TORTOISE_ORM = {
	"connections": {"default": os.environ.get("DATABASE_URL")},
	"apps": {
		"wolny": {
			"models": [
				"project.app.src.clients.model",
				"project.app.src.orders.model",
				"project.app.src.prices.model",
				"project.app.src.products.model",
				"project.app.src.store.model"
			],
			"default_connection": "default",
		},
	},
}