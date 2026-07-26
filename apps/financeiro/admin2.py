# from django.contrib import admin
# from .models import(Perfil, Conta, Categoria, Movimento, PlanejamentoFinanceiro)

# from django.contrib import messages

# from apps.financeiro.exceptions import PlanejamentoException
# from apps.financeiro.services.planejamento_service import PlanejamentoService


# @admin.register(Perfil)
# class PerfilAdmin(admin.ModelAdmin):

#     list_display = (
#         "nome",
#         "ativo",
#         "criado_em",
#     )

#     list_filter = (
#         "ativo",
#     )

#     search_fields = (
#         "nome",
#     )

#     ordering = ("nome",)

# @admin.register(Conta)
# class ContaAdmin(admin.ModelAdmin):

#     list_display = (
#         "nome",
#         "usuario",
#         "tipo",
#         "saldo_inicial",
#         "saldo_atual_display",
#         "ativo",
#         )

#     list_filter = (
#         "tipo",
#         "ativo",
#     )

#     search_fields = (
#         "nome",
#         "usuario__email",
#     )

#     ordering = ("nome",)

#     list_select_related = ("usuario",)

#     def saldo_atual_display(self, obj):
#         return f"R$ {obj.saldo_atual:,.2f}"

#     @admin.display(description="Saldo Atual")
#     def saldo_atual_display(self, obj):
#             ...

# @admin.register(Categoria)
# class CategoriaAdmin(admin.ModelAdmin):

#     list_display = (
#         "nome",
#         "usuario",
#         "tipo",
#         "ativo",
#         "criado_em",
#     )

#     list_filter = (
#         "tipo",
#         "ativo",
#     )

#     search_fields = (
#         "nome",
#         "usuario__email",
#     )

#     ordering = ("nome",)

#     list_select_related = ("usuario",)

# @admin.register(Movimento)
# class MovimentoAdmin(admin.ModelAdmin):

#     list_display = (
#         "descricao",
#         "usuario",
#         "tipo",
#         "valor",
#         "conta",
#         "categoria",
#         "data_movimento",
#         "criado_em",
#     )

#     list_filter = (
#         "tipo",
#         "data_movimento",
#     )

#     search_fields = (
#         "descricao",
#         "usuario__email",
#     )

#     date_hierarchy = "data_movimento"

#     ordering = (
#     "-data_movimento",
#     "-criado_em",
#     )

# @admin.register(PlanejamentoFinanceiro)
# class PlanejamentoFinanceiroAdmin(admin.ModelAdmin):
#     list_display = (
#     "descricao",
#     "usuario",
#     "tipo",
#     "valor",
#     "prioridade",
#     "data_prevista",
#     "status",
#     "recorrencia",
#     "parcelado",
#     )

#     list_filter = (
#     "tipo",
#     "status",
#     "recorrencia",
#     "parcelado",
#     )

#     actions = ["marcar_como_pago"]
#     @admin.action(description="Marcar planejamento(s) como pago(s)")
#     def marcar_como_pago(self, request, queryset):

#         pagos = 0

#         for planejamento in queryset:
#             try:
#                 PlanejamentoService.marcar_como_pago(planejamento)
#                 pagos += 1

#             except PlanejamentoException as erro:
#                 self.message_user(
#                     request,
#                     f"{planejamento.descricao}: {erro}",
#                     level=messages.ERROR,
#                 )

#         if pagos:
#             self.message_user(
#                 request,
#                 f"{pagos} planejamento(s) processado(s) com sucesso.",
#                 level=messages.SUCCESS,
#             )
            
#     list_select_related = (
#     "usuario",
#     "conta",
#     "categoria",
#     )

#     search_fields = (
#         "descricao",
#         "usuario__email",
#         "categoria__nome",
#         "conta__nome",
#     )

#     date_hierarchy = "data_prevista"


