from django.db import models


# Create your models here.
class District(models.Model):
    district = models.CharField(max_length=30)

    def __str__(self):
        return self.district


class Branch(models.Model):
    branch = models.CharField(max_length=30)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch


class ApplicationForm(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(max_length=8)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    phone=models.TextField()
    email=models.EmailField()
    address=models.TextField()
    district=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    account= models.CharField(max_length=100)
    materials=models.CharField(max_length=100)