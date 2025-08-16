from django.db import models

from apps.base.models import BaseModel
from apps.company.models.validators.validate_cep import validate_cep


class Company(BaseModel):
    name = models.CharField(max_length=200)
    cep = models.CharField(max_length=8, validators=[validate_cep])
