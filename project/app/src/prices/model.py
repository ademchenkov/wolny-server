from datetime import datetime

from project.app.src.common.model import PydanticModel


class PriceRequest(PydanticModel):
	from_datetime: datetime
	full_price: str
	sale_price: str = None
	has_sale: bool