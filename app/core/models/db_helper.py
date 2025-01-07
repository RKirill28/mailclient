from typing import AsyncGenerator

from core.config import settings

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession


class DatabaseHelper:
	def __init__(
			self, 
			url: str, 
			echo: bool,
			echo_pool: bool
		):
		self.engine: AsyncEngine = create_async_engine(
			url=str(url),
			echo=echo,
			echo_pool=echo_pool
		)
		self.sessionFactory: async_sessionmaker[AsyncSession] = async_sessionmaker(
			bind=self.engine,
			autoflush=False,
			autocommit=False,
			expire_on_commit=False
		) # async_sessionmaker is class
	
	async def dispose(self):
		await self.engine.dispose()

	async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
		async with self.sessionFactory() as session:
			yield session


dbHelper = DatabaseHelper(
	url=settings.database.url,
	echo=settings.database.echo,
	echo_pool=settings.database.echo_pool
)