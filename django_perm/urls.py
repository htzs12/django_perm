"""django_perm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from apps.system import views_user
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_user.IndexView.as_view(), name='index'),
    path('login/', views_user.LoginView.as_view(), name='login'),
    path('logout/', views_user.LogoutView.as_view(), name='logout'),

    path('system/', include('apps.system.urls', namespace='system')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})
    ]