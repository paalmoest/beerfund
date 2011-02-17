from django.db import models

class BeerAccount(models.Model):
    rfid = models.IntegerField()
    credits = models.IntegerField()
    user = models.CharField(max_length=20)
    def __unicode__(self):
        return self.user

class BeerFund(models.Model):
    beercount = models.IntegerField()
    def __unicode__(self):
        return "The Vault"