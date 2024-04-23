import logging

from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from tortoise.exceptions import IntegrityError

from project.app.src.database import init_db
from project.app.src.products.service import router as products_router

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
	application = FastAPI(
		title="Wolny",
		description="Welcome to Wolny API documentation!",
		redoc_url=None,
	)
	application.include_router(products_router)

	return application


app = create_application()


@app.on_event("startup")
async def startup_event():
	logging.info("Starting up...")
	await init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
	logging.info("Shutting down...")


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
	return {"status": "ok"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
	return JSONResponse(
		status_code=exc.status_code,
		content={"message": str(exc.detail)},
	)


@app.exception_handler(IntegrityError)
async def tortoise_exception_handler(request, exc):
	return JSONResponse(
		status_code=400,
		content={"message": str(exc)},
	)
