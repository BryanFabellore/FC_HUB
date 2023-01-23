from django.urls import path
from . import views

urlpatterns = [
    path('', views.LogView.as_view(), name='log_in'),
    path('signup',views.UserCreateView.as_view(), name='signup'),
]