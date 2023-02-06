from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class FCHUBView(TemplateView):
    template_name = 'FC-ADMIN/FC-ADMIN.html'


