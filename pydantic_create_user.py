from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """Pydantic модель UserSchema"""
    id: str
    email: str = EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CreateUserRequestSchema(BaseModel):
    """Pydantic модель запроса на создание пользователя"""
    email: str = EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """Pydantic модель ответа создания пользователя"""
    created_user: UserSchema = Field(alias="user")
