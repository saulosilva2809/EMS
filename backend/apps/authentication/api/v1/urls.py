from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import SendCodeForRecoverPasswordAPI


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "send-code-for-recovery-password/",
        SendCodeForRecoverPasswordAPI.as_view(),
        name="send_code_for_recovery_password"
    ),
]
