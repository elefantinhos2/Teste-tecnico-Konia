import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser) :
    id             = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username       = models.CharField(max_length = 20, unique = True)
    first_name     = models.CharField(max_length = 50)
    last_name      = models.CharField(max_length = 50)
    updated_at     = models.DateField(auto_now = True)

    REQUIRED_FIELDS = ["first_name", "last_name"]
