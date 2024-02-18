from dataclasses import dataclass
from fastapi import FastAPI

from src.internal.router.currency import router


@dataclass(frozen=True)
class Route:
    routers: tuple

    def register_router(self, app: FastAPI):
        app.include_router(router)