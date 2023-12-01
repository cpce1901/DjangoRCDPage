from django import forms
from django_recaptcha.fields import ReCaptchaField


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

    recaptcha = ReCaptchaField()
