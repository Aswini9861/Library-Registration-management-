from cProfile import label
import email
from django.db import models

# Create your models here.
class registration(models.Model):
    email=models.EmailField(max_length=30)
    pwd=models.CharField(max_length=20)


class Book(models.Model):
    ISBN=models.CharField(max_length=30)
    title=models.CharField(max_length=50)
    auther=models.CharField(max_length=30)
    edition=models.CharField(max_length=30)