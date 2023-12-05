from apps.public.models import Message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializer import MessageSerializer, MobileTokenSerializer
from .models import MobileToken

# Create your views here.


class MobileTokenApiView(APIView):
    def get(self, request, format=None):
        snippets = MobileToken.objects.all()
        serializer = MobileTokenSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MobileTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MobileTokenDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(MobileToken, pk=pk)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MobileTokenSerializer(snippet)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MessagesApiView(APIView):
    def get(self, request, format=None):
        snippets = Message.objects.all()
        serializer = MessageSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessagesDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Message, pk=pk)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MessageSerializer(snippet)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
