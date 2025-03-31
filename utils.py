from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from core.config import settings
import os
import custom_log as log

# General JSON response to return in API response
def create_response(message: str, status_code: int, success: bool = False, **kwargs):
    """ General JSON response """
    
    return JSONResponse(
      status_code = status_code,
      content = {
          'success': success,
          'message': message,
          **jsonable_encoder(kwargs)
        }
    )

def create_local_dir(path):
  try:
    # Create upload directory if it doesn't exist
    os.makedirs(path, exist_ok=True)
  except Exception as e:
    log.set_logger("create_local_dir", f"Exception: {str(e)}", action="error")
    