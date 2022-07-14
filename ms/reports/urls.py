from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'reports'


urlpatterns = [
    path('ambiente/<int:ambiente_id>/', ChecklistsAmbientes.as_view(),name='ambiente_report'),
]