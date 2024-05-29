from django.contrib import admin
from account.models import CustomUser, Test
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Test)