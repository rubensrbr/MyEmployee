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
            "address_type",
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    # address = AddressSerializer(many=True)

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
            # "address",
        ]


class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressType
        fields = [
            "description",
        ]
