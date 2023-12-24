from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # потому что у нас есть наша функция views
from django.urls import path, include

urlpatterns = [
    #path('login/', views.user_login, name='login'), здесь у нас была наша функция, которая активировалась при входе на сайт
    path('login/', auth_views.LoginView.as_view(), name='login'),  # встроенная функция от джанго для входа
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # встроенная функция от джанго для выхода
    path('', views.dashboard, name='dashboard'),
]


