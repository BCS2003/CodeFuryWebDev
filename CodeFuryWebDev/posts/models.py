from django.db import models
from accounts.models import CustomUser


class PostModel(models.Model):
    founders = models.ManyToManyField(CustomUser, related_name='co_founders')
    startup_name = models.CharField(max_length=25, unique=True)
    short_disc = models.CharField(max_length=100)
    fin_details = models.CharField(max_length=100)
    amount = models.IntegerField()
    equity = models.IntegerField()
    detailed_disc = models.TextField()

    REQUIRED_FIELDS = ['founders', 'startup_name', 'amount', 'equity']
