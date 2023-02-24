from django.db import models
from ombor.models import Client, Mahsulot, Ombor

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField()
    sana = models.DateTimeField(auto_now_add=True)
    umumiy_summa = models.PositiveBigIntegerField()
    tolandi = models.PositiveBigIntegerField()
    nasiya =  models.PositiveBigIntegerField()