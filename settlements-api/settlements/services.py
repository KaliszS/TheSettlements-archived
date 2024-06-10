from uuid import UUID

from pydantic import BaseModel

from settlements.database import Base, DbSession

type ModelType[model: Base] = model
type CreateSchemaType[schema: BaseModel] = schema
type UpdateSchemaType[schema: BaseModel] = schema


class CrudServices[ModelType, CreateSchemaType, UpdateSchemaType]:
    def __init__(self, model: type[ModelType]):
        self.model = model

    def create(self, db_session: DbSession, creator: CreateSchemaType) -> ModelType:
        creation_data = creator.model_dump()
        creation = self.model(**creation_data)
        db_session.add(creation)
        db_session.commit()
        db_session.refresh(creation)
        return creation

    def get(self, db_session: DbSession, object_id: UUID | int) -> ModelType | None:
        return db_session.query(self.model).filter(self.model.id == object_id).one_or_none()

    def update(
        self,
        db_session: DbSession,
        originator: ModelType,
        updater: UpdateSchemaType,
    ) -> ModelType:
        updater_data = updater.model_dump(exclude_none=True)
        for field_name, field_value in updater_data.items():
            setattr(originator, field_name, field_value)
        db_session.add(originator)
        db_session.commit()
        db_session.refresh(originator)
        return originator

    def delete(self, db_session: DbSession, object_id: UUID | int) -> ModelType | None:
        originator = self.get(db_session, object_id)
        db_session.delete(originator)
        db_session.commit()
        return originator


class AppServices[CrudModelType: CrudServices, ModelType, CreateSchemaType, UpdateSchemaType]:
    def __init__(self, crudModel: type[CrudModelType], model: type[ModelType]):
        self.crud = crudModel(model)
        self.name = self.crud.model.__name__.lower()

    def create(self, db_session: DbSession, creator: CreateSchemaType) -> ModelType:
        creation = self.crud.create(db_session, creator)
        return creation

    def get(self, db_session: DbSession, object_id: UUID | int, raise_404=True) -> ModelType | None:
        fetch = self.crud.get(db_session, object_id)
        return fetch

    def update(
        self,
        db_session: DbSession,
        originator: ModelType,
        updater: UpdateSchemaType,
    ) -> ModelType:
        fetch = self.crud.update(db_session, originator, updater)
        return fetch

    def delete(self, db_session: DbSession, object_id: UUID | int) -> ModelType | None:
        deletion = self.crud.delete(db_session, object_id)
        return deletion
