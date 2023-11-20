# subscriptions/models.py
from django.db import models

class Subscription(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=255)
    active = models.BooleanField(default=False)