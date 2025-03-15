from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url="postgres://postgres:test_password@postgres_db:5432/test_database",
        modules={"models": ["database.models"]}
    )
    await Tortoise.generate_schemas()
