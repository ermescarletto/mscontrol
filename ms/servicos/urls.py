from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'api'

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('checklist/',ChecklistView.as_view(),name='checklist'),
    path('checklist/<int:entidade_id>/<int:checklist_id>/', ChecklistFormView.as_view(),name='checklist_servico'),
    path('login/',LoginView.as_view(),name='login'),
    path('dashboard/',login_required(DashboardView.as_view()),name='dashboard'),
    path('qrcode/<int:checklist_id>/<int:ambiente_id>/', login_required(QrCodeView.as_view()), name='qrcode')
]