from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from src.configuration.routes import __routes__
from src.internal.event.startup import on_startup, on_loop_startup


class Server:
    __app: FastAPI

    def __init__(self, app: FastAPI):
        self.__app = app
        self.__register_route(app)
        self.__register_events(app)

    def get_app(self) -> FastAPI:
        return self.__app

    @staticmethod
    def __register_events(app):
        app.on_event('startup')(repeat_every(seconds=60 * 60 * 12)(on_startup))
        app.on_event('startup')(repeat_every(seconds=5)(on_loop_startup))

    @staticmethod
    def __register_route(app):
        __routes__.register_router(app)
