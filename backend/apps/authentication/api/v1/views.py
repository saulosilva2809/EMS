import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SendCodeForRecoverPasswordSerializer
from .service.send_code_for_recovery_password import (
    SendCodeForRecoveryPasswordService
)


logger = logging.getLogger(__name__)


class SendCodeForRecoverPasswordAPI(APIView):
    def post(self, request):
        serializer = SendCodeForRecoverPasswordSerializer(data=request.data)

        if serializer.is_valid():
            service = SendCodeForRecoveryPasswordService(serializer)
            email = service.get_field('email')

            try:
                service.generate_code()
                service.save_code_in_cache(email=email)
                service.send_email_to_user(email=email)

                return Response({
                    'success': 'True',
                    'message': f'E-mail enviado para {email} com sucesso!'
                }, status=status.HTTP_200_OK)
        
            except Exception as e:
                logger.error(f'Erro ao enviar email: {str(e)}')

                return Response({
                    'success': 'False',
                    'message': f'Erro ao enviar email para {email}, tente novamente mais tarde!'
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
