from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import FormView
from django_recaptcha.client import RecaptchaResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.private.models import MobileToken
from .form import ContactForm
from .models import Message
import json
import requests



# Create your views here.
class Contact(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def send_message(self, title, body):
        expo_token = MobileToken.objects.first()
        message = {"to": expo_token.token, "title": title, "body": body}
        return requests.post("https://exp.host/--/api/v2/push/send", json=message)

    def form_valid(self, form):
        recaptcha_response = self.request.POST.get("g-recaptcha-response", "")
        recaptcha_result = RecaptchaResponse(recaptcha_response)

        if recaptcha_result.is_valid:
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            code_phone = form.cleaned_data["code"]
            phone = form.cleaned_data["phone"]
            address = form.cleaned_data["address"]
            details = form.cleaned_data["details"]
            phone_completed = str(code_phone) + str(phone)

            message = Message(
                name=name,
                email=email,
                phone=phone_completed,
                address=address,
                details=details,
            )
            message.save()

            name = name.replace("Ñ", "N").replace("ñ", "n")
            address = name.replace("Ñ", "N").replace("ñ", "n")
            details = name.replace("Ñ", "N").replace("ñ", "n")

            payload = {
                "name": name,
                "email": email,
                "phone": phone_completed,
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

            return redirect(reverse("contact_app:contact") + "?ok")


