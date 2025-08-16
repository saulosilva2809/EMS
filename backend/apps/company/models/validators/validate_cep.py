from django.core.exceptions import ValidationError


def validate_cep(self, cep: str):
    if not self.isdigit() or len(cep) != 8:
        raise ValidationError({"cep": "The postal code must contain 8 numeric digits"})
