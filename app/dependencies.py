from app.repositories.InMemoryRepository.in_memory_user_repository import InMemoryUserRepository
from app.services.user_service import UserService

_repo = InMemoryUserRepository()
_service = UserService(_repo)

def get_user_service() -> UserService:
    return _service