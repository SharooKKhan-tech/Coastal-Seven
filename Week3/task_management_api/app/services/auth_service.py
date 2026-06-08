from app.repositories.user_repository import UserRepository

from app.core.security import (
    verify_password,
    create_access_token
)


class AuthService:

    def __init__(self):
        self.repo = UserRepository()

    async def login(
        self,
        db,
        email,
        password
    ):
        user = await self.repo.get_by_email(
            db,
            email
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password
        ):
            return None

        token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return token