import logging

from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings
class MongoDataBase:

    def __init__(self, client: AsyncIOMotorClient = None, database: str = None):
        self.client = client
        self.database = database

    def connect(self, database_uri: str = None, database_port: str = None):
        self.client = AsyncIOMotorClient(database_uri, database_port)

    def close(self):
        self.client.close()

    def get_database(self, database_name: str = None):
        self.database = database_name

db = MongoDataBase()
db.connect(settings.MONGODB_DATABASE_URI, settings.PORT)
db.get_database(settings.MONGO_DATABASE_NAME)