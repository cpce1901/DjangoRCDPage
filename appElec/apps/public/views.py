from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse
from apps.private.models import Logo, MobileToken
from .form import ContactForm
from .models import Message
import json
import requests as r
from django.conf import settings

# Import the reCAPTCHA package
from django_recaptcha.client import RecaptchaResponse


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

    def send_message(self, title, body):
        expo_token = MobileToken.objects.first()
        message = {"to": expo_token.token, "title": title, "body": body}
        return r.post("https://exp.host/--/api/v2/push/send", json=message)

    def form_valid(self, form):
      
        recaptcha_response = self.request.POST.get("g-recaptcha-response")
        recaptcha_secret_key = settings.RECAPTCHA_SECRET_KEY
        recaptcha_url = "https://www.google.com/recaptcha/api/siteverify"

        recaptcha_data = {
            "secret": recaptcha_secret_key,
            "response": recaptcha_response,
        }

        is_valid = r.post(recaptcha_url, data=recaptcha_data).json()

        if is_valid:
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = self.request.POST.get("phone")
            address = form.cleaned_data["address"]
            details = form.cleaned_data["details"]

            message = Message(
                name=name, email=email, phone=phone, address=address, details=details
            )
            message.save()

            name = name.replace("Ñ", "N").replace("ñ", "n")
            address = name.replace("Ñ", "N").replace("ñ", "n")
            details = name.replace("Ñ", "N").replace("ñ", "n")

            payload = {
                "name": name,
                "email": email,
                "phone": phone,
                "address": address,
                "details": details,
            }

            payload = json.dumps(payload)

            titulo = "Pagina - Contacto"
            mensaje = f"Haz recibido un nuevo mensjae en tu pagina web de: {name}"

            try:
                self.send_message(titulo, mensaje)
            except:
                print("No se ha enviado la notificación")

            return redirect(reverse("public_app:contact") + "?ok")

        
