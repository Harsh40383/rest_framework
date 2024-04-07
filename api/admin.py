from django.contrib import admin
from api.models import Company, Employee

# this classes for admin pannel costomization
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email' , 'company')
    search_fields = ('name',)
    list_filter = ('company',)

# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
