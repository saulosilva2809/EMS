from apps.authentication.models import User
from rest_framework import serializers


class SendCodeForRecoverPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Nenhum usuário encontrado com esse e-mail.")
        return value
