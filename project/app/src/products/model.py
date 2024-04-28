from typing import List
from typing import Optional

from project.app.src.common.model import PydanticModel


class ProductDescription(PydanticModel):
	title: str
	text: str


class ProductAdvantage(PydanticModel):
	text: str


class ProductImage(PydanticModel):
	url: str


class Product(PydanticModel):
	name: str


class ProductPreview(Product):
	id: str
	descriptions: Optional[List[ProductDescription]] = []
	advantages: Optional[List[ProductAdvantage]] = []
	images: Optional[List[ProductImage]] = []