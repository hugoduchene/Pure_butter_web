"""Pure_butter_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from substitute import views
from user import views as views_connect
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('myfood', views.get_product_record, name='myfood'),
    path('save', views.save_food, name='save'),
    path('account', views_connect.accountView, name='account'),
    path('logout', auth_views.LogoutView.as_view(next_page='/registration'), name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('registration', views_connect.registrationView, name='registration'),
    path('meat/<name_product>', views.search_meat, name='meat'),
    path('result', views.result, name='result'),
    path('', views.index, name='index'),
    path('admin', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
