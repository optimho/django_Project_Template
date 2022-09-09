import os
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProTwo.settings')
import django
django.setup()

from AppTwo.models import User_List



django.setup()
fake = Faker()


def add_users(n=5):
    for new_user in range(n):
        user_name = fake.name()
        user_last_name = fake.last_name()
        user_email = fake.email()

        fake_users = User_List.objects.get_or_create(first_name=user_name, last_name=user_last_name, email=user_email)[0]
        fake_users.save()


if __name__ == "__main__":
    print("Populating database")
    add_users(5)
    print("complete adding users to the database")
