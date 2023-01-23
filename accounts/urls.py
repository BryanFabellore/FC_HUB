from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountsView.as_view()),
    path('users',views.AccountsView.list),
    path('users/<int:pk>',views.AccountsView.user),
    
   
]