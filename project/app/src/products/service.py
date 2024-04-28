from typing import List

from fastapi import APIRouter, status
from tortoise.transactions import in_transaction

from project.app.src.products.model import ProductAdvantage
from project.app.src.products.model import ProductDescription
from project.app.src.products.model import ProductImage
from project.app.src.products.model import Product
from project.app.src.products.model import ProductPreview

from project.app.src.products.db_model import ProductDb, ProductImageDb, ProductAdvantageDb, ProductDescriptionDb

router = APIRouter(
	prefix="/v1/products",
	tags=["Products"],
)


# Products
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Product)
async def create_product(product: Product):
	new_product = await ProductDb.create_with_id(**product.dict())
	return new_product


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ProductPreview])
async def get_all_products():
	products = await ProductDb.filter(is_deleted=False).all().prefetch_related('images', 'advantages', 'descriptions')
	return [ProductPreview.from_orm(product) for product in products]


@router.put("/{product_id}", status_code=status.HTTP_200_OK, response_model=Product)
async def update_product(product_id: str, product: Product):
	async with in_transaction():
		existing_product = await ProductDb.filter(id=product_id).select_for_update().first()
		await existing_product.update_from_dict(dict(product)).save()
	return existing_product


# Product descriptions
@router.post("/{product_id}/descriptions", status_code=status.HTTP_201_CREATED, response_model=ProductDescription)
async def create_product_description(product_id: str, product_description: ProductDescription):
	new_product_description = await ProductDescriptionDb.create_with_id(
		**product_description.dict(),
		product_id=product_id
	)
	return new_product_description


# Product advantages
@router.post("/{product_id}/advantages", status_code=status.HTTP_201_CREATED, response_model=ProductAdvantage)
async def create_product_advantage(product_id: str, product_advantage: ProductAdvantage):
	new_product_advantage = await ProductAdvantageDb.create_with_id(
		**product_advantage.dict(),
		product_id=product_id
	)
	return new_product_advantage


# Product images
@router.post("/{product_id}/images", status_code=status.HTTP_201_CREATED, response_model=ProductImage)
async def create_product_image(product_id: str, product_image: ProductImage):
	new_product_image = await ProductImageDb.create_with_id(
		**product_image.dict(),
		product_id=product_id
	)
	return new_product_image
