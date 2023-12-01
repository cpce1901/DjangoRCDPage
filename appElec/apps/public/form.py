from django import forms
from django.core.validators import RegexValidator
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.conf import settings
import re


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "id": "name",
                "placeholder": "Ingresa tu nombre",
                "class": "text-input",
            }
        ),
    )

    email = forms.EmailField(  # Cambiado a EmailField para validar correos electrónicos
        label="Correo electrónico",
        max_length=100,
        widget=forms.EmailInput(  # Cambiado a EmailInput
            attrs={
                "id": "email",
                "placeholder": "Ingresa tu correo",
                "class": "text-input",
            }
        ),
    )

    phone = forms.CharField(
        min_length=6,
        label="Teléfono",
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "id": "phone",
                "placeholder": "Ingresa tu número de teléfono",
                "class": "text-input",
            }
        ),
    )

    address = forms.CharField(
        label="Dirección",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "id": "address",
                "placeholder": "Ingresa tu dirección",
                "class": "text-input",
            }
        ),
    )

    details = forms.CharField(
        label="Detalles",
        max_length=512,
        widget=forms.Textarea(
            attrs={
                "id": "details",
                "rows": 8,
                "placeholder": "Ingresa los detalles porfavor...",
                "class": "text-input",
            }
        ),
    )


    recaptcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_SITE_KEY,
        private_key=settings.RECAPTCHA_SECRET_KEY,
        widget=ReCaptchaV2Checkbox(),
        error_messages={"required": settings.RECAPTCHA_ERROR_MSG["required"]},
    )

    def clean_phone(self):
        numero = self.cleaned_data["phone"]
        # Verificar si la entrada consiste solo en dígitos
        if not numero.isdigit():
            raise forms.ValidationError("Ingrese solo números...")

        # Verificar la longitud del número
        if len(numero) < 6 or len(numero) > 10:
            raise forms.ValidationError("El número debe tener entre 6 y 10 dígitos.")

        return numero
