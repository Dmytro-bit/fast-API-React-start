from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    MONGO_DB_URI: str
    MONGO_DB_NAME: str
    CLOUDINARY_SECRET_KEY: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_CLOUD_NAME: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
