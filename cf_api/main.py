from fastapi import FastAPI

from cf_api.core.config import API_KEY, API_PREFIX, APP_NAME, APP_VERSION, IS_DEBUG
from cf_api.core.event_handler import start_app_handler, stop_app_handler
from cf_api.api.routes.router_cf import router

def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    fast_app.include_router(router, prefix=API_PREFIX)

    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))

    return fast_app


app = get_app()
