from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage.as_view(), name='personal_inf'),
    path('personal_inf/', views.PersonalInf.as_view()),
    path('news/', include('app_users.urls')),
    path('login', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
