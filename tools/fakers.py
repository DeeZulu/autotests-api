import time
from faker import Faker


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"


class Fake:

    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        return self.faker.text()

    def uuid4(self) -> str:
        return self.faker.uuid4()

    def email(self) -> str:
        return self.faker.email()

    def sentence(self) -> str:
        return self.faker.sentence()

    def password(self) -> str:
        return self.faker.password()

    def last_name(self) -> str:
        return self.faker.last_name()

    def first_name(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.first_name()

    def estimated_time(self) -> str:
        return f"{self.rand_int()} weeks"

    def rand_int(self, start: int = 1, end: int = 100) -> int:
        return self.faker.random_int(start, end)

    def min_score(self) -> int:
        return self.rand_int(1, 30)

    def max_score(self) -> int:
        return self.rand_int(50, 100)

fake = Fake(faker=Faker())
