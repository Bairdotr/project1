from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length =400)

    def __str__(self):
        return self.name

class Certificate_Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Grade(models.Model):
    type = models.CharField(max_length=4)

    def __str__(self):
        return self.type

class Faculty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):

    full_name = models.CharField(max_length=60)
    year_of_graduation = models.DateField(default = datetime.today)
    department = models.ForeignKey(Department, on_delete=CASCADE)
    grade = models.ForeignKey(Grade, on_delete=CASCADE)
    school = models.ForeignKey(School, on_delete=CASCADE)
    certificate_type = models.ForeignKey(Certificate_Type, on_delete=CASCADE)

    def __str__(self):
        return self.full_name
