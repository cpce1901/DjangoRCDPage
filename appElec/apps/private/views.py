from django.shortcuts import render
from apps.public.models import Menssage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializer import MessageSerializer, MobileTokenSerializer
from .models import MobileToken

# Create your views here.


class MobileTokenList(ListAPIView):
    serializer_class = MobileTokenSerializer

    def get_queryset(self):
        queryset = MobileToken.objects.all()
        return queryset


class MobileTokenAdd(CreateAPIView):
    serializer_class = MobileTokenSerializer


class MessagesApi(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Menssage.objects.all().order_by("-created")[:10]
        return queryset


class MessageDetailApi(RetrieveAPIView):
    serializer_class = MessageSerializer
    queryset = Menssage.objects.all()


class MessageAddApi(CreateAPIView):
    serializer_class = MessageSerializer


class MessageUpdateApi(UpdateAPIView):
    serializer_class = MessageSerializer


class MessageDeleteApi(DestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Menssage.objects.all()
