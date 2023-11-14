from django.shortcuts import render
from apps.public.models import Menssage
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializer import MessageSerializer

# Create your views here.


class MessagesApi(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Menssage.objects.all().order_by("created")[:10]
        return queryset


class MessageDetailApi(RetrieveAPIView):
    serializer_class = MessageSerializer


class MessageAddApi(CreateAPIView):
    serializer_class = MessageSerializer


class MessageUpdateApi(UpdateAPIView):
    serializer_class = MessageSerializer


class MessageDeleteApi(DestroyAPIView):
    serializer_class = MessageSerializer
