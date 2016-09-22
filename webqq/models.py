from django.db import models
from bbs.models import UserProfile
# Create your models here.


class QQGroup(models.Model):
    name = models.CharField(max_length=64)
    founder = models.ForeignKey(UserProfile)
    admins = models.ManyToManyField(UserProfile, related_name='admins')
    members = models.ManyToManyField(UserProfile, related_name='members')
    mem_limits = models.IntegerField(default=200)
    descriptions = models.TextField(max_length=256)

    def __str__(self):
        return self.name



