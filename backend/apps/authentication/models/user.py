from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.company.models import Company


class User(AbstractUser):
    TYPE_CHOICES = [
        ("manager", "Manager"),
        ("employee", "Employee"),
    ]

    CARGO_CHOICES = [
        ("intern", "Estagiário"),
        ("junior_dev", "Desenvolvedor Júnior"),
        ("mid_dev", "Desenvolvedor Pleno"),
        ("senior_dev", "Desenvolvedor Sênior"),
        ("tech_lead", "Tech Lead"),
        ("qa", "Analista de QA"),
        ("devops", "DevOps"),
        ("product_manager", "Product Manager"),
        ("designer", "Designer UX/UI"),
        ("cto", "CTO"),
    ]

    type = models.CharField(max_length=8, choices=TYPE_CHOICES, null=True, blank=True)
    company = models.OneToOneField(Company, on_delete=models.PROTECT, null=True, blank=True)
    cargo = models.CharField(max_length=30, choices=CARGO_CHOICES, null=True, blank=True)
