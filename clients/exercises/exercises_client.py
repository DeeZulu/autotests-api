from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """Структура объекта задания"""
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQueryDict(TypedDict):
    """Структура запроса получения заданий"""
    courseId: str

class GetExercisesResponseDict(TypedDict):
    """Структура ответа с заданиями"""
    exercises: list[Exercise]

class CreateExerciseRequestDict(TypedDict):
    """Структура запроса создания задания"""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """Структура запроса обновления задания"""
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """Клиент для работы с сервисом заданий"""

    def get_exercises_api(self, course_id: str) -> Response:
        """
        Получение списка заданий для определенного курса.
        :param course_id: ID определённого курса
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.get(f'/api/v1/exercises/{course_id}')
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id
        :param exercise_id:
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.get(f'/api/v1/exercises/{exercise_id}')
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создание задания.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response =  self.post(f'/api/v1/exercises', request)
        return response.json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновления данных задания.
        :param exercise_id: ID задания
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.patch(f'/api/v1/exercises/{exercise_id}', request)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания.
        :param exercise_id: ID задания
        :return: Ответ от сервера в виде объекта httpx_examples.Response
        """
        response = self.delete(f'/api/v1/exercises/{exercise_id}')
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию CoursesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
