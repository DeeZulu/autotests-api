from httpx import Client


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx_examples.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx_examples.Client.
    """
    return Client(timeout=100, base_url="http://localhost:8000")