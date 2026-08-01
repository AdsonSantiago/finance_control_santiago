from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from apps.authentication.viewsets.auth_viewset import (
    LoginView,
)

urlpatterns = [

    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),

    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="refresh",
    ),
]