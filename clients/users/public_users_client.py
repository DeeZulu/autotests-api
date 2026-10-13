from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Выполняет POST-запрос к эндпоинту /api/v1/users для создания пользователя
        :return: Объект httpx_examples.Response с данными ответа.
        """
        return self.post('/api/v1/users', json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate(response.json())

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
