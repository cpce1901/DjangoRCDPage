from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = 'public/home.html'

# Create your views here.
class About(TemplateView):
    template_name = 'public/about.html'

# Create your views here.
class Services(TemplateView):
    template_name = 'public/services.html'

# Create your views here.
class Contact(TemplateView):
    template_name = 'public/contact.html'
   
