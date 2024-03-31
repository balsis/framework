import os
import random

from data.data import Person, Color
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        salary=random.randint(20000, 200000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn()
    )


def generated_file():
    path = f"{os.path.dirname(os.getcwd())}/filetest{random.randint(0, 99)}.txt"
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 99)}')
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
        )
