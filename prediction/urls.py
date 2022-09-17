"""prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path,include
# from django.views.generic.base import TemplateView as view
from stockprediction import views
urlpatterns = [
    path("", views.homepage, name="home"),
    path("admin/", admin.site.urls),
    path("login/", views.account_login, name="login"),
    path("logout/", views.account_logout, name="logout"),
    path("register/", views.register_request, name="register"),
    path('controlpanel/',views.controlpanel,name='controlpanel'),
    path('search/',views.controlpanel,name='controlpanel'),
    path('research/',views.research ,name='research'),
    path('analysis/predictValue',views.predictValue,name='predictValue'),
    path('analysis/',views.analysis,name='analysis'),
]
