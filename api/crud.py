from utils import create_response

async def get_search_results(request_body):
    """ Search the results based on user query """
    try:
        user_query = request_body.user_query
        # Some code
        result_data = {}
        return create_response(message="Results are fetched successfully", status_code=200, success=True, data=result_data)
    except Exception as e:
        return create_response(message=str(e), status_code=500, success=False, data={})
    