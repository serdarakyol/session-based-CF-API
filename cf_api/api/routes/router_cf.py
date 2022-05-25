from starlette.requests import Request
from fastapi import APIRouter, Depends

from cf_api.core import security
from cf_api.models.model_cf import CFRequest, CFResponse
from cf_api.services.service_cf import Recommendation

router = APIRouter()

@router.post("/collaborativefilter", response_model=CFResponse, name="collaborative filter")
async def post_recommend(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    request_data: CFRequest = None,
    ) -> CFResponse:

    # load word2vec model
    recommendation_service = Recommendation(data=request.app.state.data)
    # get similar top n item
    results = recommendation_service.recommend(items=request_data.item, n_item=request_data.n_item)
    return CFResponse(input_item=request_data.item, similar_items=results)
