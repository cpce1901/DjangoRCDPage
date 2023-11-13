from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse
from django.conf import settings
from apps.private.models import Logo
from .form import ContactForm
from .models import Menssage

import json
from django.http import JsonResponse
from appElec.mqtt import client as mqtt_client


# Create your views here.
class Home(TemplateView):
    template_name = "public/home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        logo = Logo.objects.filter(name="logo")
        context["logo"] = logo
        return context


# Create your views here.
class About(TemplateView):
    template_name = "public/about.html"


# Create your views here.
class Services(TemplateView):
    template_name = "public/services.html"


# Create your views here.
class Contact(FormView):
    template_name = "public/contact.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        phone = self.request.POST.get("phone")
        address = form.cleaned_data["address"]
        details = form.cleaned_data["details"]

        message = Menssage(
            name=name, email=email, phone=phone, address=address, details=details
        )
        message.save()

        name = name.replace('Ñ', 'N').replace('ñ', 'n')
        address = name.replace('Ñ', 'N').replace('ñ', 'n')
        details = name.replace('Ñ', 'N').replace('ñ', 'n')

        payload = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "details": details,
        }

        payload = json.dumps(payload)

        mqtt_client.publish(settings.MQTT_TOPIC, payload, 1)

        return redirect(reverse("public_app:contact") + "?ok")
