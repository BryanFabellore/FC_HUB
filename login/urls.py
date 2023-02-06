from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginInterfaceView.as_view(), name='log_in'),
    path('signup',views.UserCreateView.as_view(), name='signup'),
]