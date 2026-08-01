from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from apps.authentication.serializers.login_serializer import LoginSerializer


class LoginView(TokenObtainPairView):

    serializer_class = LoginSerializer