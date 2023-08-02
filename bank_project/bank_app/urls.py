from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('form/', views.form, name='form'),
    path('msg/', views.msg, name='msg'),

]