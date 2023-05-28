from django.contrib import admin
from firstapp.models import Employee
# Register your models here.

class EmplAdmin(admin.ModelAdmin):
    list_display = ['firstName','lasstName']

admin.site.register(Employee,EmplAdmin);
