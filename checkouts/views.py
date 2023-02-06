from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class CheckoutsView(TemplateView):
    template_name ='checkouts/checkouts.html'
    
  
    
