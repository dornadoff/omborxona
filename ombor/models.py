from django.db import models
from django.contrib.auth.models import User

class Ombor(models.Model):
    nom = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    tel = models.CharField(max_length=14)
    ism = models.CharField(max_length=100)
    manzil = models.CharField(max_length=100)

class Mahsulot(models.Model):
    nom = models.CharField(max_length=500)
    brend = models.CharField(max_length=500)
    narx = models.FloatField()
    kelgan_sana = models.DateField()
    miqdor = models.CharField(max_length=100)
    olchov = models.CharField(max_length=100)

class Client(models.Model):
    ism = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    manzil = models.CharField(max_length=100)
    tel = models.CharField(max_length=14)
    qarz = models.FloatField()
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)


