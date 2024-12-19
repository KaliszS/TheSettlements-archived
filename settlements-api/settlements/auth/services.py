from typing import Annotated

from fastapi import Depends, HTTPException, status

from settlements.database import DbSession
from settlements.auth.utils import oauth2_scheme


class AuthServices:
    def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        user = "user1"
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Invalid credentials", 
                headers={"WWW-Authenticate": "Bearer"}
            )
        


auth_services = AuthServices()