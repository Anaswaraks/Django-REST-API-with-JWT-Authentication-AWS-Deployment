from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return self.name
    

