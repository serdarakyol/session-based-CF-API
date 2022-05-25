from fastapi import APIRouter

from cf_api.api.routes import router_cf

api_router = APIRouter()
api_router.include_router(router_cf.router, tags=["semantic_search"], prefix="/semanticsearch")
