from typing import List
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.utils import serializer_helpers
from rest_framework.filters import OrderingFilter
from .serializers import AddressTypeSerializer, EmployeeSerializer
from .models import AddressType, Employee


class EmployeeViewList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = [
        "start_date",
        "last_name",
    ]
    ordering = ["last_name"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployeeViewDetail(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AddressTypeViewList(ListCreateAPIView):
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeSerializer
