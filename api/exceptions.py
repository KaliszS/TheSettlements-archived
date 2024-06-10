from fastapi import HTTPException


def collection_not_found(collection, results):
    if not results:
        raise HTTPException(status_code=404, detail=f"No {collection.name} found")


def document_not_found(collection, id):
    raise HTTPException(
        status_code=404, detail=f"{collection.name} with an ID {id} not found"
    )
