from typing import List
from uuid import uuid4
from app.repositories.user_repository import IUserRepository
from app.models.user import User

class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.users_by_id = {}
        self.user_id_by_email = {}

    def create_user(self, user: User) -> User:
        if user.email in self.user_id_by_email:
            raise ValueError("Email already exists")

        user.id = str(uuid4())

        self.users_by_id[user.id] = user
        self.user_id_by_email[user.email] = user.id
        return user

    def get_user_by_id(self, user_id: str) -> User | None:
        return self.users_by_id.get(user_id)

    def get_users(self, offset: int, limit: int) -> List[User]:
        users = list(self.users_by_id.values())
        return users[offset: offset + limit]

    def update_user(self, user_id: str, data: dict) -> User | None:
        user = self.users_by_id.get(user_id)
        if not user:
            return None

        if "email" in data:
            new_email = data["email"]
        if new_email != user.email:  
            if new_email in self.user_id_by_email:
                raise ValueError("Email already exists")
            del self.user_id_by_email[user.email]
            self.user_id_by_email[new_email] = user.id

        for key, value in data.items():
            setattr(user, key, value)

        return user
