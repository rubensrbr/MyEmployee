from django.urls import path
from .views import AddressTypeViewList, EmployeeViewList, EmployeeViewDetail


urlpatterns = [
    path(
        "employees/",
        EmployeeViewList.as_view(),
        name="employees-list",
    ),
    path(
        "employees/int:<pk>/",
        EmployeeViewDetail.as_view(),
        name="employees-detail",
    ),
    path(
        "address_type/",
        AddressTypeViewList.as_view(),
        name="address-type-list",
    ),
]
