from django.core.cache import cache
from django.template.loader import render_to_string
from random import randint
from rest_framework.serializers import Serializer

from apps.base.base_service import BaseService
from apps.tasks.tasks import send_email


class SendCodeForRecoveryPasswordService(BaseService):
    def __init__(self, serializer: Serializer):
        super().__init__(serializer)
        self.code = None
        self.version = 'v1'       

    def generate_code(self):
        self.code = str(randint(0, 99999)).zfill(5)
    
    def save_code_in_cache(self, email):
        if not self.code:
            raise ValueError('Not code')

        cache.set(f'recovery_code_{email}', self.code, timeout=900)

    def send_email_to_user(self, email):
        if not self.code:
            raise ValueError('Not code')

        send_email.delay(
            subject='Código para Recuparação de Senha - EMS',
            message=None,
            recipient_list=[email],
            html_message=render_to_string(f'email/{self.version}/send_code_for_recovery_password.html', {
                    'code': self.code
            })
        )
