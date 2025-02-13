from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class JobTitleType(models.Model):
    description = models.CharField(
        max_length=30,
    )

    class Meta:
        db_table = "job_title_type"

    def __str__(self):
        return f"{self.description}"


class Employee(models.Model):
    first_name = models.CharField(
        max_length=100,
    )
    last_name = models.CharField(
        max_length=100,
    )
    birth_date = models.DateField()
    start_date = models.DateField()
    photo = models.ImageField(
        upload_to="uploads/%Y/%m/%d/",
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.DO_NOTHING,
    )
    job_title = models.ForeignKey(
        JobTitleType,
        on_delete=models.CASCADE,
        related_name="employees",
    )

    class Meta:
        db_table = "employee"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AddressType(models.Model):
    description = models.CharField(
        max_length=100,
    )

    class Meta:
        db_table = "address type"

    def __str__(self):
        return f"{self.description}"


class Address(models.Model):
    state_province = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=50,
    )
    postal_code = models.CharField(
        max_length=10,
    )
    city = models.CharField(
        max_length=100,
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="addresses",
    )
    type_address = models.ForeignKey(
        AddressType,
        on_delete=models.CASCADE,
        related_name="addresses",
    )

    class Meta:
        db_table = "address"

    def __str__(self):
        return f"{self.country} - {self.state_province} - {self.city}"
