from datetime import timedelta
from typing import Annotated, List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select

from app.core.auth import authenticate, create_access_token
from app.core.config import settings
from app.core.deps import SessionDep
from app.models import Token, User

app = FastAPI()


@app.get("/users/")
def read_users(session: SessionDep) -> List[User]:
    """
    Retrieve users.
    """
    statement = select(User)
    users = session.exec(statement).all()
    return users


@app.post("/login/access-token")
def login_access_token(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = authenticate(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=create_access_token(user.id, expires_delta=access_token_expires)
    )
