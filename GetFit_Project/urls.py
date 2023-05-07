"""
URL configuration for GetFit_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from GetFit.views import index,home,RegisterView
from django.contrib.auth.views import LoginView, LogoutView
from GetFit.views import user_list
from GetFit import views
from django.contrib.auth import views as auth_views
from GetFit.views import user_profile




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('users/', user_list, name='user_list'),
    path('home/', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    
]
