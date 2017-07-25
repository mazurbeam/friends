from __future__ import unicode_literals
from ..login.models import User
from django.db import models

# Create your models here.

class Friend(models.Model):
    friends = models.ManyToManyField(User)
