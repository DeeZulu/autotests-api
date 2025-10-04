from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


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
        :return: Объект httpx_examples.Response с данными ответа.
        """
        return self.post('/api/v1/users', json=request)

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
