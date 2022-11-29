import motor.motor_asyncio

from app.core.config import settings

mongo_driver = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_DATABASE_URI, settings.PORT)

db = mongo_driver[settings.DATABASE_NAME]