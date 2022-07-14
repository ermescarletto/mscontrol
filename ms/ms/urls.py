"""ms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import sys
from django.contrib import admin, auth
from django.urls import path,include
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
from django.core.management import execute_from_command_line
from servicos.views import IndexView

admin.site.site_header = 'MS Control'
admin.site.index_title = 'Administração do Sistema'
admin.site.site_title = 'MS Control'


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('user/', include('django.contrib.auth.urls')),  # new
    path('api/', include('api.urls', namespace='api')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('control/', include('servicos.urls', namespace='control')),
    path('reports/', include('reports.urls', namespace='reports')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
