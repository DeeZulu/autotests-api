from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """Описание структуры запроса на аутентификацию."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Выполняет POST-запрос к эндпоинту /api/v1/users для создания пользователя
        :return: Объект httpx.Response с данными ответа.
        """
        return self.post('/api/v1/users', json=request)

client = PublicUsersClient()