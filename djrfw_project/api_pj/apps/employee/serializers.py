from rest_framework import serializers
from .models import Employee, Address, AddressType, JobTitleType


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "country",
            "state_province",
            "city",
            "postal_code",
            "employee",
            "type_address",
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    # addresses = AddressSerializer(many=True)

    class Meta:

        model = Employee
        fields = (
            "id",
            "first_name",
            "last_name",
            "birth_date",
            "job_title",
            "start_date",
            "user",
            "photo",
            # "addresses",
        )


class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressType
        fields = [
            "description",
        ]


class BasicAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "country",
            "state_province",
            "city",
            "postal_code",
            "employee",
            "type_address",
        ]


class BasicEmployeeSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "first_name",
            "last_name",
            "birth_date",
            "job_title",
            "start_date",
            "user",
            "photo",
            "addresses",
        ]
