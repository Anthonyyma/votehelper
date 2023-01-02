from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# class Neighbourhood(models.Model):
#     name = models.TextField() 

class Voter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    name = models.TextField()
    address = models.TextField()
    email = models.TextField(default="", blank=True)
    phone = models.TextField(default="", blank=True)
    neighbourhood = models.TextField(default="", blank=True)
    assignedEmp = models.TextField(default="", blank=True)
    decision = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)

# get queryset of all childmodel instances that are related to that parentmodel
# parent_instance = ParentModel.objects.get(id=1)
# child_instances = parent_instance.childmodel_set.all()
