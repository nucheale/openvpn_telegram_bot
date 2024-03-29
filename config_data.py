from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    SSH_IP: SecretStr
    SSH_USERNAME: SecretStr
    SSH_PASSWORD: SecretStr
    # DATABASE_FILE: str
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()
