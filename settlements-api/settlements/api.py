from fastapi import APIRouter, Depends

from settlements.auth.utils import oauth2_scheme
from settlements.users.views import router as users_router
from settlements.games.views import router as games_router
from settlements.cities.views import router as cities_router


api_router = APIRouter(dependencies=[Depends(oauth2_scheme)])


api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(games_router, prefix="/games", tags=["games"])
api_router.include_router(cities_router, prefix="/cities", tags=["cities"])
