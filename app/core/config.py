from pydantic import BaseModel
from pydantic_settings import BaseSettings

class DatabaseConfig(BaseModel):
	host: str = 'postgres'
	port: int = 5432
	db_name: str = 'email'
	db_user: str = 'postgres'
	db_pass: str = 'postgres'
	url: str = f'postgresql+asyncpg://{db_user}:{db_pass}@{host}:{port}/{db_name}"'

class SQLAlchemyConfig(BaseModel):
	echo: bool = True
	echo_pool: bool = False

class RunConfig(BaseModel):
	host: str = '0.0.0.0'
	port: int = 8000

class ApiPrefixConfig(BaseModel):
	api_prefix: str = '/api'

class Settings(BaseSettings):
	run: RunConfig = RunConfig()
	api: ApiPrefixConfig = ApiPrefixConfig()
	database: DatabaseConfig = DatabaseConfig()
	sqla: SQLAlchemyConfig = SQLAlchemyConfig()


settings = Settings()