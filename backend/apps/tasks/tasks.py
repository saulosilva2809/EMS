from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3, 'countdown': 60})
def send_email(self, subject, message, recipient_list, from_email=None, html_message=None):
    """
    Celery task para envio de emails
    
    Args:
        subject (str): Assunto do email
        message (str): Mensagem em texto plano
        recipient_list (list): Lista de destinatários
        from_email (str, optional): Email do remetente. Defaults to DEFAULT_FROM_EMAIL.
        html_message (str, optional): Mensagem em HTML. Defaults to None.
    
    Returns:
        dict: Resultado do envio
    """
    try:
        if from_email is None:
            from_email = settings.DEFAULT_FROM_EMAIL
        
        result = send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False
        )
        
        logger.info(f"Email enviado com sucesso para {recipient_list}")
        return {
            'success': True,
            'message': f'Email enviado para {len(recipient_list)} destinatário(s)',
            'recipients': recipient_list,
            'result': result
        }
        
    except Exception as exc:
        logger.error(f"Erro ao enviar email para {recipient_list}: {str(exc)}")
        
        # Retry automático em caso de erro
        if self.request.retries < self.max_retries:
            logger.info(f"Tentativa {self.request.retries + 1} de {self.max_retries + 1}")
            raise self.retry(exc=exc)
        
        return {
            'success': False,
            'message': f'Erro ao enviar email: {str(exc)}',
            'recipients': recipient_list,
            'error': str(exc)
        }
