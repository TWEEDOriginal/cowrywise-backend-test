from datetime import datetime as dt
from django.db import models
import uuid

# Create your models here.


class UUID_table(models.Model):
    key = models.DateTimeField(auto_now_add=True)
    value = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ["-key"]

    def __str__(self):
        return f"id == {self.id} dict == {self.key} : {self.value}"
