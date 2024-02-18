from src.configuration.routes.routes import Route
from src.internal.router import currency


__routes__ = Route(routers=(currency.router))
