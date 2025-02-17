from typing import ClassVar

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseConfig(BaseModel):
	url: PostgresDsn
	echo: bool
	echo_pool: bool

class RunConfig(BaseModel):
	host: str = '0.0.0.0'
	port: int = 8000

class ApiV1PrefixConfig(BaseModel):
	prefix: str = '/v1'
	email_addresses_prefix: str = '/email_addresses'
	messages_prefix: str = '/messages'

class ApiPrefixConfig(BaseModel):
	api_prefix: str = '/api'
	v1: ApiV1PrefixConfig = ApiV1PrefixConfig()

class Settings(BaseSettings):
	model_config: ClassVar = SettingsConfigDict(
		env_file=('.env.template', '.env'),
		case_sensitive=False,
		env_nested_delimiter='__',
		env_prefix='CONFIG__'
	)

	run: RunConfig = RunConfig()
	api: ApiPrefixConfig = ApiPrefixConfig()
	database: DatabaseConfig


settings = Settings()