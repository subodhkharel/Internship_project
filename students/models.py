from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=200)
    joined_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
