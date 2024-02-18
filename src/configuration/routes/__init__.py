from src.configuration.routes.routes import Route
from src.internal.router.currency import router as currency_router


__routes__ = Route(routers=(currency_router))
