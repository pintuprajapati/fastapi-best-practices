from fastapi import APIRouter, Request
from api.schemas import SearchSchema
from api import crud

router = APIRouter(tags=["Search"])

@router.post("/search")
async def get_search_results(request: Request, request_body: SearchSchema):
    """ Search API to get the relevant results based on user query """
    
    search_results = await crud.get_search_results(request_body)
    return search_results
    

