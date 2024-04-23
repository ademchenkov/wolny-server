from typing import List, Optional

from pydantic import UUID4

from project.app.src.common.model import PydanticModel


class ProductDescription(PydanticModel):
	title: str
	text: str


class ProductAdvantage(PydanticModel):
	text: str


class ProductImage(PydanticModel):
	url: str


class ProductRequest(PydanticModel):
	name: str
	images: Optional[List[ProductImage]]
	advantages: Optional[List[ProductAdvantage]]
	descriptions: Optional[List[ProductDescription]]


class ProductResponse(ProductRequest):
	id: UUID4
