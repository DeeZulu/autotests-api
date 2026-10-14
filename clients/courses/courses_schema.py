from pydantic import BaseModel, ConfigDict, Field
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса
    """
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    createdByUser: UserSchema = Field(alias="createdByUser")


class GetCoursesRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class GetCoursesResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос информации о курсе
    """
    courses: list[CourseSchema]


class GetCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос информации о курсе
    """
    course: CourseSchema


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса создания курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    maxScore: int = Field(alias="maxScore")
    minScore: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления курса
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")
