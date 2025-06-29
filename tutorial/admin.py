from django.contrib import admin
from .models import Studennt,Employee
# Register your models here.
# admin.site.register(Studennt) # it will show object only

@admin.register(Studennt)  
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll'] # by this we can see a table like structure

# admin.site.register(Employee)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'city', 'age')