from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # URL para obter um novo token de acesso
    path(
        "authentication/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    # URL para atualizar um token de acesso
    path(
        "authentication/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    # URL para verificar a validade de um token de acesso
    path(
        "authentication/token/verify/",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
]
