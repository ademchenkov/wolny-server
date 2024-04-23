from typing import List

from fastapi import APIRouter, status

from project.app.src.products.model import ProductRequest, ProductResponse
from project.app.src.products.db_model import Product, ProductImage, ProductAdvantage, ProductDescription

router = APIRouter(
	prefix="/products",
	tags=["Products"],
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductResponse)
async def create_product(product: ProductRequest):
	new_product = await Product.create(**product.dict(
		exclude={"images", "advantages", "descriptions"}
	))

	for image in product.images:
		await ProductImage.create(**image.dict(), product=new_product)

	for advantage in product.advantages:
		await ProductAdvantage.create(**advantage.dict(), product=new_product)

	for description in product.descriptions:
		await ProductDescription.create(**description.dict(), product=new_product)

	new_product = await Product.get(id=new_product.id).prefetch_related('images', 'advantages', 'descriptions')

	return new_product


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ProductResponse])
async def get_all_products():
	products = await Product.filter(is_deleted=False).all().prefetch_related('images', 'advantages', 'descriptions')

	return [ProductResponse.from_orm(product) for product in products]
