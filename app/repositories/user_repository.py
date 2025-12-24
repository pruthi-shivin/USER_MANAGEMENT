from abc import ABC, abstractmethod
from typing import List
from app.models.user import User


class IUserRepository(ABC):

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> User | None:
        pass

    @abstractmethod
    def get_users(self, offset: int, limit: int) -> List[User]:
        pass

    @abstractmethod
    def update_user(self, user_id: str, data: dict) -> User | None:
        pass
