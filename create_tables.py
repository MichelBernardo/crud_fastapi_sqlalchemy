from core.configs import settings
from core.database import engine



async def create_tables() -> None:
    import models.__all_models
    print('Creating the database tables...')

    async with engine.begin() as connection:
        await connection.run_sync(settings.DBBaseModel.metadata.drop_all)
        await connection.run_sync(settings.DBBaseModel.metadata.create_all)
    
    print('Tables created successfully.')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())