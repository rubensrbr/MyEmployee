from django.urls import include, path
from .views import (
    AddressTypeViewSet,
    AddressViewSet,
    BasicEmployeeView,
    EmployeeViewSet,
    BasicAdressView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employees")
router.register(r"addresses", AddressViewSet, basename="addresses")
router.register(r"address_type", AddressTypeViewSet, basename="address_type")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "basic_employee/<int:pk>",
        BasicEmployeeView.as_view(),
        name="basic_employee",
    ),
    path(
        "basic_addresses/<int:pk>",
        BasicAdressView.as_view(),
        name="basic_addresses",
    ),
]
