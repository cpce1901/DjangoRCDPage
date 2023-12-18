from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Budgets, Items
from .serializer import BudgetsSerializer, ItemsSerializer


class BudgetsApiView(APIView):
    def get(self, request, format=None):
        snippets = Budgets.objects.all()
        serializer = BudgetsSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BudgetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BudgetsDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Budgets, pk=pk)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BudgetsSerializer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BudgetsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemsApiView(APIView):
    def get(self, request, format=None):
        snippets = Items.objects.all()
        serializer = ItemsSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemsDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Items, pk=pk)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ItemsSerializer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ItemsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


