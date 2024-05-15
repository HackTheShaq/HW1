from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Dron


class HomeView(TemplateView):
    template_name = 'home.html'
class AboutView(TemplateView):
    template_name = 'about.html'


class DronesView(TemplateView):
    template_name = 'drones.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['drones'] = Dron.objects.all()
        return context
    
    