from django.urls import path
from . import views

urlpatterns = [
    path('', views.session_page, name='session_page'),
    path('session_login/', views.session_login, name='session_login'),
    path('cookie/', views.cookie_page, name='cookie_page'),
    path('cookie_login/', views.cookie_login, name='cookie_login'),
]
