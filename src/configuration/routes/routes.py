from dataclasses import dataclass
from fastapi import FastAPI


@dataclass
class Route:
    routers: tuple

    def register_router(self, app: FastAPI):
        for router in self.routers:
            app.include_router(router)