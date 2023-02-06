from django.urls import path
from . import views

urlpatterns = [
    path('',views.CheckoutsView.as_view(), name='checkouts'),   
]