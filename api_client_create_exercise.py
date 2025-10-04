from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import CreateUserRequestDict, get_public_users_client

from tools.fakers import get_random_email

create_new_user_req = CreateUserRequestDict(
    email=get_random_email(),
    password="1234",
    lastName="LName",
    firstName="FName",
    middleName="No"
)

new_user = get_public_users_client().create_user_api(request=create_new_user_req).json()
auth_data = AuthenticationUserDict(email=create_new_user_req["email"], password=create_new_user_req["password"])

files_client = get_files_client(user=auth_data)
exercises_client = get_exercises_client(user=auth_data)
courses_client = get_courses_client(user=auth_data)

new_file = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./test_data/image.png"
)

files_result = files_client.create_file(request=new_file)
print(f"Create file data: {files_result}")

new_course = CreateCourseRequestDict(
    title="Test",
    maxScore=99,
    minScore=10,
    description="TestTest",
    estimatedTime="one week",
    previewFileId=files_result["file"]["id"],
    createdByUserId=new_user["user"]["id"]
)

course_result = courses_client.create_course_api(request=new_course)
print(f"Create course data: {course_result}")

new_exercise = CreateExerciseRequestDict(
    title= "Test",
    courseId= course_result["course"]["id"],
    maxScore= 15,
    minScore= 0,
    orderIndex= 1,
    description= "Test Exercise",
    estimatedTime= "30"
)
exercise_result = exercises_client.create_exercise_api(request=new_exercise)
print(f"Create exercise data: {exercise_result}")
