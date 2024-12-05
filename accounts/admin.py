from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Redactor

admin.site.register(Redactor, UserAdmin)
