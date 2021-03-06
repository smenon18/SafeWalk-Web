from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

from datetime import datetime

# Create your models here.

class User(models.Model):
    password = models.CharField(max_length=32, null=False, blank=False)
    email = models.CharField(max_length=64, null=False, blank=False, unique=True)

    def get_email(self):
        return self.email

class ParentalRel(models.Model):
    class Meta:
        unique_together = (('child', 'parent'),)
    child = models.ForeignKey(User, on_delete=models.CASCADE, related_name='child')
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parent')

    def get_child(self):
        return self.child

    def get_parent(self):
        return self.parent

class InTransit(models.Model):
    child = models.ForeignKey(User, on_delete=models.CASCADE)
    depart_time = models.DateTimeField(default=now)
    expected_arrival_time = models.DateTimeField()
    has_arrived = models.BooleanField(default=False)
    est_distance= models.PositiveIntegerField(default=0)
    start_pos= models.CharField(max_length=255, default=0)
    end_pos= models.CharField(max_length=255, default=0)

    def get_child(self):
        return self.child
    
    def get_depart_time(self):
        return self.depart_time

    def get_expected_arrival_time(self):
        return self.expected_arrival_time

    def get_has_arrived(self):
        return self.has_arrived
