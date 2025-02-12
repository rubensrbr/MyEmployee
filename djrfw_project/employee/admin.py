from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Employee, Address, AddressType, JobTitleType


admin.site.register(CustomUser, UserAdmin)
admin.site.register([Employee, Address, AddressType, JobTitleType])
