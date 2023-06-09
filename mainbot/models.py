from django.db import models

# Create your models here.


class Threadlist(models.Model):
    api_key = models.CharField(max_length=30)
    secret_key = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    min_val = models.IntegerField(default=0)
    max_val = models.IntegerField(default=10)
    interval_time = models.IntegerField(default=10)
    marketing_symbol = models.CharField(max_length=20)
    crypto_remain = models.CharField(max_length=30)
