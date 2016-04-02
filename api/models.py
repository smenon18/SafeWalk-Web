from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32, unique=True, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)
    acctype = models.BooleanField(default=False) # False is child, True is parent

class ParentalRel(models.Model):
    childUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='child')
    parentUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parent')
