from django.db import models
from django.contrib.auth.models import User
from client.models import Client
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='project_client')
    created_by = models.ForeignKey(User, related_name='project_creator', on_delete=models.PROTECT)
    assigned_users = models.ManyToManyField(User, related_name='assigned_users')

    def __str__(self):
        return self.name