from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name