from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vote  = models.IntegerField(default=0)
    accumulate = models.IntegerField(default=0)

    # vote_today = models.IntegerField(default=0)
    # vote_week = models.IntegerField(default=0)
    # vote_month = models.IntegerField(default=0)
    '''
    def __str__(self):
        return self.user
    '''
