from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView
from django_recaptcha.client import RecaptchaResponse
from .form import ContactForm
from .models import Message, MobileToken
import json
import requests


# Create your views here.
class Contact(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def send_message(self, title, body):
        token_users = MobileToken.objects.all()
        token_users = [token.token for token in token_users]
        headers = {
            "host": "exp.host",
            "accept": "application/json",
            "accept-encoding": "gzip, deflate",
            "Content-Type": "application/json",
        }

        message = {"to": token_users, "title": title, "body": body}

        return requests.post(
            "https://exp.host/--/api/v2/push/send", headers=headers, json=message
        )

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
