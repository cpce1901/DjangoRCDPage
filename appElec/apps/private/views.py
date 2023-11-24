from django.shortcuts import render
from apps.public.models import Menssage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import MessageSerializer, MobileTokenSerializer
from .models import MobileToken

# Create your views here.


class MobileTokenView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            # Recuperación de un objeto específico por ID
            queryset = MobileToken.objects.filter(pk=pk)
            if not queryset.exists():
                return Response(
                    {"error": "MobileToken not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            # Lista todos los objetos si no se proporciona un ID
            queryset = MobileToken.objects.all()

        serializer = MobileTokenSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MobileTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        try:
            instance = MobileToken.objects.get(pk=pk)
        except MobileToken.DoesNotExist:
            return Response(
                {"error": "MobileToken not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = MobileTokenSerializer(instance)
        original_data = serializer.data

        serializer = MobileTokenSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"original_data": original_data, "updated_data": serializer.data}
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = MobileToken.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MessagesView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            # Recuperación de un objeto específico por ID
            queryset = Menssage.objects.filter(pk=pk)
            if not queryset.exists():
                return Response(
                    {"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            # Lista todos los objetos si no se proporciona un ID
            queryset = Menssage.objects.all()

        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        try:
            instance = Menssage.objects.get(pk=pk)
        except Menssage.DoesNotExist:
            return Response(
                {"error": "Menssage not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = MessageSerializer(instance)
        original_data = serializer.data

        serializer = MessageSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"original_data": original_data, "updated_data": serializer.data}
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = Menssage.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
