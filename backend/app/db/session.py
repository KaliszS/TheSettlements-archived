from motor.motor_asyncio import AsyncIOMotorClient
from neo4j import GraphDatabase

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
db.connect(settings.MONGODB_DATABASE_URI, settings.MONGO_PORT)
db.get_database(settings.MONGO_DATABASE_NAME)

class Neo4jDataBase:
    def __init__(self, driver = None):
        self.driver = driver

    def connect(self, database_uri: str = None, user: str = None, password: str = None):
        self.driver = GraphDatabase.driver(database_uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def open_session(self, cypher: str = None):
        with self.driver.session() as session:
            result = session.run(query=cypher)

        return result

# db = Neo4jDataBase()
# db.connect(settings.NEO4J_DATABASE_URI, settings.NEO4J_USER, settings.NEO4J_PASSWORD)
