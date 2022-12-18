from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Voter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    address = models.TextField()
    decision = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)

# class AddressGroups(models.Model):
    