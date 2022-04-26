from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'api'

urlpatterns = [
    path('check/<int:ambiente_id>/', ChecklistsAmbienteView.as_view(),name='checklist_servico'),
    path('login/',LoginView.as_view(),name='login'),
    path('dashboard/',login_required(DashboardView.as_view()),name='dashboard'),
    path('qrcode/<int:ambiente_id>/', login_required(QrCodeView.as_view()), name='qrcode'),
    path('ambientes/',AmbientesView.as_view(), name='ambientes'),
    path('entidades/',EntidadesView.as_view(), name='entidades'),
    path('entidades/<pk>/delete/',EntidadeDelete.as_view(), name='deleta_entidade'),
    path('servicos/',ServicosView.as_view(), name='servicos'),
    path('api/check/', APIChecklistPreenchido.as_view(), name='checklist_preenchido'),
    path('check/form/<int:ambiente_id>/<int:checklist_id>/',FormChecklistView.as_view(),name='form_checklist'),
    path('checklists/', ChecklistsView.as_view(),name='checklists')
]