from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioChangeForm, UsuarioCreationForm
from .models import Perfil, Usuario


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "nome",
        "ativo",
    )

    search_fields = (
        "nome",
    )


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario

    ordering = ("email",)

    list_display = (
        "email",
        "nome",
        "sobrenome",
        "perfil",
        "timezone",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "perfil",
        "timezone",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "codigo",
        "email",
        "nome",
        "sobrenome",
    )

    fieldsets = (
        (
            "Informações",
            {
                "fields": (
                    "email",
                    "password",
                    "nome",
                    "sobrenome",
                    "perfil",
                    "timezone",
                )
            },
        ),
        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Datas",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "nome",
                    "sobrenome",
                    "perfil",
                    "timezone",
                    "password1",
                    "password2",
                ),
            },
        ),
    )