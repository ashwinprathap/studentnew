from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phno=models.CharField(max_length=10)
    address=models.CharField(max_length=400)
    place=models.CharField(max_length=100)

    def __str__(self):
        return self.name