from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SendCodeForRecoverPasswordSerializer
from apps.authentication.service.generate_code import generate_code
from apps.tasks.tasks import send_email


class SendCodeForRecoverPasswordAPI(APIView):
    def post(self, request):
        serializer = SendCodeForRecoverPasswordSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = generate_code()

            try:
                send_email.delay(
                    subjetc='Código para Recuparação de Senha - EMS',
                    message=None,
                    recipient_list=[email],
                    html_message=render_to_string('email/send_code_for_recovery_password.html', {
                        'code': code
                    })
                )
                return Response({
                    'success': True,
                    'message': f'E-mail enviado para {email} com sucesso!'
                }, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({
                    'success': False,
                    'message': str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
