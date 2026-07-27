from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.financeiro.viewsets.conta_viewset import ContaViewSet
from apps.financeiro.viewsets.categoria_viewset import CategoriaViewSet
from apps.financeiro.viewsets.movimento_viewset import MovimentoViewSet
from apps.financeiro.viewsets.planejamento_viewset import PlanejamentoViewSet
from apps.financeiro.viewsets.extrato_viewset import ExtratoViewSet
from apps.financeiro.viewsets.dashboard_viewset import DashboardViewSet

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/financeiro/",
        include("apps.financeiro.urls")
    ),
]

router = DefaultRouter()

router.register(
    "contas",
    ContaViewSet,
    basename="conta"
)

router.register(
    "categorias",
    CategoriaViewSet,
    basename="categoria"
)

router.register(
    "movimentos",
    MovimentoViewSet,
    basename="movimento"
)

router.register(
    "planejamentos",
    PlanejamentoViewSet,
    basename="planejamento"
)

router.register(
    "extrato",
    ExtratoViewSet,
    basename="extrato"
)

router.register(
    "dashboard",
    DashboardViewSet,
    basename="dashboard"
)

urlpatterns = router.urls