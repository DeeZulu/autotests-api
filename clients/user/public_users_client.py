from httpx import Response

from clients.api_client import APIClient


class CreateUserDict:
    """Описание структуры запроса на аутентификацию."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):

    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Выполняет POST-запрос к эндпоинту /api/v1/users для создания пользователя
        :return: Объект httpx.Response с данными ответа.
        """
        url = '/api/v1/users'
        return self.client.post(url=url, json=request)
