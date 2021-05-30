from django.contrib import admin
from .models import School, Student, Certificate_Type, Grade, Department, Faculty

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Certificate_Type)
admin.site.register(Grade)
admin.site.register(Department)
admin.site.register(Faculty)
