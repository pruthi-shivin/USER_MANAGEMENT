from datetime import datetime
from typing import List
from app.models.user import User
from app.repositories.user_repository import IUserRepository


class UserService:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def create_user(self, data: dict) -> User:
        user = User(
            id="",  
            created_at=datetime.utcnow(),
            **data
        )
        return self.repo.create_user(user)

    def get_user(self, user_id: str) -> User | None:
        return self.repo.get_user_by_id(user_id)

    def get_users(self, page: int, limit: int) -> List[User]:
        offset = (page - 1) * limit
        return self.repo.get_users(offset, limit)

    def update_user(self, user_id: str, data: dict) -> User | None:
        return self.repo.update_user(user_id, data)
