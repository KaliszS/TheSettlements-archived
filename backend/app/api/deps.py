from app.db.session import db
from app.utils import filename

def getCollection(fileObject):
    collectionName = filename.getFileName(fileObject)

    return db[collectionName]