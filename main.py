from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.responses import RedirectResponse
import uvicorn

from app.Settings.config import settings
from app.Database.database import SessionLocal

# Create the FastAPI app
app = FastAPI(
    title=settings.SERVER_NAME,
    description="Example of API with celery and rabbitMQ",
    redoc_url=False,
    root_path=settings.API_PATH_VERSION,
    version=settings.SERVER_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/docs", include_in_schema=False)
def overridden_swagger():
    return get_swagger_ui_html(openapi_url="/openapi.json", title=settings.SERVER_NAME)


@app.middleware("http")
async def db_session_middlewa(request: Request, call_next):
    response = Response("Internal server erro", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app)
