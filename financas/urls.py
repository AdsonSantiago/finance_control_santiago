from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/financeiro/", include("apps.financeiro.urls")),
    # path("api/usuarios/", include("apps.usuarios.urls")),

    path(
    "api/auth/",
    include("apps.authentication.urls"),
    ),

]