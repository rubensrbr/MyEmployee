from typing import List
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from .serializers import (
    AddressSerializer,
    AddressTypeSerializer,
    BasicAddressSerializer,
    BasicEmployeeSerializer,
    EmployeeSerializer,
)
from .models import Address, AddressType, Employee
from .permissions import IsAdmin, IsEmployeeOwner


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = [
        "start_date",
        "last_name",
    ]
    ordering = ["last_name"]
    permission_classes = [IsAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BasicEmployeeView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = BasicEmployeeSerializer
    permission_classes = [IsEmployeeOwner]


class BasicAdressView(RetrieveUpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = BasicAddressSerializer
    permission_classes = [IsEmployeeOwner]


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAdmin]


class AddressTypeViewSet(ModelViewSet):
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeSerializer
    permission_classes = [IsAdmin]
