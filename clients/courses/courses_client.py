
from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.courses.courses_schema import (CreateCourseRequestSchema, GetCoursesRequestSchema,
                                            UpdateCourseRequestSchema,
                                            UpdateCourseResponseSchema, CreateCourseResponseSchema,
                                            GetCourseResponseSchema)


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    BASE_PATH = "/api/v1/courses"

    def get_courses_api(self, query: GetCoursesRequestSchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Pydantic схема.
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.get(
            self.BASE_PATH,
            params=query.model_dump(by_alias=True)
        )
        return response

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.get(
            f"{self.BASE_PATH}{course_id}")
        return response

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.post(
            self.BASE_PATH,
            json=request.model_dump(by_alias=True)
        )
        return response

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response =  self.patch(
            f"{self.BASE_PATH}{course_id}",
            json=request.model_dump(by_alias=True)
        )
        return response

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.delete(
            f"{self.BASE_PATH}{course_id}"
        )
        return response.json()

    def get_course(self, course_id: str) -> GetCourseResponseSchema:
        response = self.get_course_api(course_id)
        return GetCourseResponseSchema.model_validate_json(response.text)

    def create_course(self, request: CreateCourseRequestSchema):
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def update_course(self, course_id: str, request: UpdateCourseRequestSchema):
        response = self.update_course_api(course_id, request)
        return UpdateCourseResponseSchema.model_validate_json(response.text)

    def delete_course(self, course_id: str):
        response = self.delete_course_api(course_id)
        return response.json()


# Добавляем builder для CoursesClient
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))