from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class ProductsView(TemplateView):
    template_name ='products/products.html'
    
  
    
class BlockoutView(TemplateView):
    template_name ='products/blockout.html'  
    

class fiveNoneView(TemplateView):
    template_name ='products/fiveNone.html'  
    
class threeNoneView(TemplateView):
    template_name ='products/threeNone.html'  
    
class tiebackView(TemplateView):
    template_name ='products/tieback.html'  