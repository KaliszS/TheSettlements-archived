from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.api import exceptions


async def create(model_in, collection):
    model_dict = jsonable_encoder(model_in)
    model_created = await collection.insert_one(model_dict)
    model_out = await collection.find_one({"_id": model_created.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=model_out)


async def read_all(collection, skip=0, limit=100):
    results = await collection.find().skip(skip).to_list(limit)

    exceptions.collection_not_found(collection, results)

    return results


async def read_by_id(id, collection):
    if (model_out := await collection.find_one({"_id": id})) is not None:
        return model_out

    exceptions.document_not_found(collection, id)


async def update(id, model_in, collection):
    model_in = {k: v for k, v in model_in.dict().items() if v is not None}

    if len(model_in) >= 1:
        update_result = await collection.update_one({"_id": id}, {"$set": model_in})

        if update_result.modified_count == 1:
            if (model_out := await collection.find_one({"_id": id})) is not None:
                return model_out

    if (model_unaltered := await collection.find_one({"_id": id})) is not None:
        return model_unaltered

    exceptions.document_not_found(collection, id)


async def delete_all(collection):
    delete_result = await collection.delete_many({})

    if delete_result.deleted_count >= 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content="")

    exceptions.collection_not_found(collection, delete_result.deleted_count)


async def delete(id, collection):
    delete_result = await collection.delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content="")

    exceptions.document_not_found(collection, id)
