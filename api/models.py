from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32, unique=True, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)
    email = models.CharField(max_length=64, null=False, blank=False)

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username


class ParentalRel(models.Model):
    class Meta:
        unique_together = (('child', 'parent'),)
    child = models.ForeignKey(User, on_delete=models.CASCADE, related_name='child')
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parent')

    def get_child(self):
        return self.child

    def get_parent(self):
        return self.parent
