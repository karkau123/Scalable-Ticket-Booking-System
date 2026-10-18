"""Process liveness endpoint."""

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health", summary="Check API liveness")
async def liveness() -> dict[str, str]:
    """Report that the API can serve requests without checking external services."""
    return {"status": "ok"}
