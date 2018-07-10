from django.contrib import admin

# Register your models here.
from account.models import UserORM

admin.site.register(UserORM)