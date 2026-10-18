"""Application entry point for the Scalable Ticket Booking System API."""

from fastapi import FastAPI

from services.api.app.routes.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Scalable Ticket Booking System",
        description="An event ticket booking API, built incrementally.",
        version="0.1.0",
    )
    app.include_router(health_router, prefix="/api/v1")
    return app


app = create_app()
