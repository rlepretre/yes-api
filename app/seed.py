from app.core.auth import get_password_hash
from app.core.db import engine
from app.models import SQLModel, User
from sqlalchemy.orm import Session


def seed_database():
    with Session(engine) as session:
        yesman = User(id=1, email="yes@man.com", full_name="YesMan", hashed_password=get_password_hash("yes"))
        session.add(yesman)

        session.commit()


if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    seed_database()
