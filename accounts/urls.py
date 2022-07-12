from django.urls import path
from . import views

urlpatterns = [
    path('Register/', views.RegisterFormView.as_view(), name='Register'),
    path('Login/', views.LoginFormView.as_view(), name='Login'),
    path('Logout/', views.LogoutView.as_view(), name='Logout')
]
