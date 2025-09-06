from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class CreateExerciseRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):

    def get_exercises_api(self, course_id: str) -> Response:
        """
        Получение списка заданий для определенного курса.
        :param course_id: ID определённого курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{course_id}')

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id
        :param exercise_id:
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создание задания.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f'/api/v1/exercises', request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновления данных задания.
        :param exercise_id: ID задания
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания.
        :param exercise_id: ID задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

