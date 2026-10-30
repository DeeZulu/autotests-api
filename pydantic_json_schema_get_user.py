from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

public_user_client = get_public_users_client()
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_user_client.create_user(create_user_request)
user = create_user_response.user

private_user_client = get_private_users_client(
    user=AuthenticationUserSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
)
get_user_response_schema = GetUserResponseSchema.model_json_schema()
get_user_response = private_user_client.get_user_api(user.id).json()
validate_json_schema(
    instance=get_user_response,
    schema=get_user_response_schema
)
