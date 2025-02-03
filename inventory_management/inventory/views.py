from django.shortcuts import render
from django.views.generic import TemplateView

# Basic homepage
class Index (TemplateView):
    template_name = 'inventory/index.html'

