"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from app1 import views as app1_views
from maps import views as maps_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', app1_views.details, name = 'register'),
    path('locate/',maps_views.input, name = "locate_yourself"),
    #path("login/", app1_views.login_request, name="login"),
    #path("logout/", app1_views.logout_request, name="logout"),
    #url(r'^login/$', auth_views.login, {'template_name': 'app1/login.html'}, name='login'),
   url( r'^login/$',auth_views.LoginView.as_view(template_name="app1/login.html"), name="login"),
   path('list/<int:pk>/',maps_views.list, name="list"),
   #path('', include('currLocation.urls')),
   #path("logout/", views.logout_request, name="logout"),

]
