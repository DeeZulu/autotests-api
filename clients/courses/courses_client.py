from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.get("/api/v1/courses", params=query)
        return response.json()

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.get(f"/api/v1/courses/{course_id}")
        return response.json()

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.post("/api/v1/courses", json=request)
        return response.json()

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response =  self.patch(f"/api/v1/courses/{course_id}", json=request)
        return response.json()

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.delete(f"/api/v1/courses/{course_id}")
        return response.json()

    def get_course(self, course_id: str):
        response = self.get_course_api(course_id)
        return response.json()

    def create_course(self, request: CreateCourseRequestDict):
        response = self.create_course_api(request)
        return response.json()

    def update_course(self, course_id: str, request: UpdateCourseRequestDict):
        response = self.update_course_api(course_id, request)
        return response.json()

    def delete_course(self, course_id: str):
        response = self.delete_course_api(course_id)
        return response.json()




# Добавляем builder для CoursesClient
def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))