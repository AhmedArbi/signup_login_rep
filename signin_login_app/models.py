from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    user_name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    date_of_birth = models.DateField()


