import random
from faker import Faker
from django.core.management.base import BaseCommand
from employee.models import CustomUser, Employee


# class Command(BaseCommand):
#     help = "Generates employees"
#
#     def handle(self, *args, **options):
#         fake = Faker()
#
#         # get the user
#         # user = CustomUser.objects.filter(username="admin").first()
#         user = CustomUser.objects.create_superuser(
#             username="admin",
#             password="admin",
#         )
