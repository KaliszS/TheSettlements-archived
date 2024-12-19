from settlements.services import CrudServices, AppServices
from settlements.users.models import User
from settlements.users.schemas import UserCreate, UserUpdate
from settlements.database import DbSession


class UserCrud(CrudServices[User, UserCreate, UserUpdate]):
    def get_by_name(self, db_session: DbSession, name: str) -> User | None:
        return db_session.query(self.model).filter(self.model.name == name).one_or_none()


class UserServices(AppServices[UserCrud, User, UserCreate, UserUpdate]):
    def get_by_name(self, db_session: DbSession, name: str) -> User | None:
        return self.crud.get_by_name(db_session, name)


user_services = UserServices(UserCrud, User)
