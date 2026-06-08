from app.db.models.user import User
from app.core.security import hash_password
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self):
        self.repo = UserRepository()

    async def create_user(
        self,
        db,
        data
    ):
        user = User(
            name=data.name,
            email=data.email,
            password=hash_password(data.password)
        )

        return await self.repo.create(
            db,
            user
        )