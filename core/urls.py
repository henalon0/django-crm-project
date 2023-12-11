from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('password_reset_request', views.password_reset_request, name='password_reset_request'),
    path('password_reset/<uidb64>/<token>', views.password_reset, name='password_reset'),
    path('register', views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('logout', views.logout, name='logout'),
    path('create', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
