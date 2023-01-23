from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductsView.as_view(), name='products'),
    path('blockout',views.BlockoutView.as_view(), name='blockout'),
    path('fiveNone',views.fiveNoneView.as_view(), name='fiveNone'),
    path('threeNone',views.threeNoneView.as_view(), name='threeNone'),
    path('tieback',views.tiebackView.as_view(), name='tieback'),
   
]