from django.contrib import admin
from .models import Manager,Employee
# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('mName',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('mName','eName')

admin.site.register(Manager,ManagerAdmin)
admin.site.register(Employee,EmployeeAdmin)
