import uuid

from django.db import models

# Create your models here.

class Item(models.Model): 
    id        = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
    name      = models.CharField(max_length = 125, unique = True)
    create_at = models.DateTimeField(auto_now_add = True)
