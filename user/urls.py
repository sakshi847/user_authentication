from django.urls import path
from django.shortcuts import redirect
from .views import signup_view, login_view, dashboard_view, logout_view, password_reset_view, password_reset_confirm_view

urlpatterns = [
    path('', lambda request: redirect('login')),  
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('password-reset/', password_reset_view, name='password_reset'),
    path('password-reset-confirm/<str:email>/', password_reset_confirm_view, name='password_reset_confirm'),
]