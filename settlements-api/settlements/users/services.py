from settlements.services import CrudServices, AppServices
from settlements.users.models import User
from settlements.users.schemas import UserCreate, UserUpdate


class UserCrud(CrudServices[User, UserCreate, UserUpdate]):
    pass


class UserServices(AppServices[UserCrud, User, UserCreate, UserUpdate]):
    pass


user_services = UserServices(UserCrud, User)
