from src.core.configs import settings
from src.core.database import engine

async def create_tables() -> None:
    import src.models.__all_models
    print("Criando as tabelas no banco de dados...")
    
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tabelas criadas...")
    
if __name__ == '__main__':
    import asyncio
    print(">>>")
    asyncio.run(create_tables())