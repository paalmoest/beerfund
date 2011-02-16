from django.db import models

class BeerAccount(models.Model):
    rfid = models.IntegerField()
    credits = models.IntegerField()
    user = models.CharField(max_length=20)


