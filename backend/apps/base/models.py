import uuid

from django.db import models


class BaseModel(models.Model):
    code = models.UUIDField(default=uuid.uuid4())
