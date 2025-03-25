from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API Settings
    API_ACCESS_TOKEN: str
    ENVIRONMENT: str
        
    # Application Settings
    DEBUG: bool = False
    APP_NAME: str = "project-name"

    # Redis Settings
    REDIS_URL: str

    # OpenAI Settings
    OPENAI_API_KEY: str
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "allow"

@lru_cache()
def get_settings():
    return Settings()

# Load settings
settings = get_settings() 
