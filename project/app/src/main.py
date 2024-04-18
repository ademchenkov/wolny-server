import logging

from fastapi import FastAPI

from project.app.src.database import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
	application = FastAPI(
		title="Wolny",
		description="Welcome to Wolny API documentation!",
		redoc_url=None,
	)

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
