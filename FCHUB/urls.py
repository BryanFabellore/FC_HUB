from django.urls import path
from . import views

urlpatterns = [
    path('', views.FCHUBView.as_view(),name='FCHUB'),
   
]