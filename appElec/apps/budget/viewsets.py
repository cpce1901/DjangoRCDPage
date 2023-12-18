from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import ClientsSerializer, ItemsSerializer, BudgetsSerializer


class ClientsViewSet(ModelViewSet):
    serializer_class = ClientsSerializer
    queryset = ClientsSerializer.Meta.model.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Provider guardado con exito... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemsViewSet(ModelViewSet):
    serializer_class = ItemsSerializer
    queryset = ItemsSerializer.Meta.model.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Provider guardado con exito... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BudgetsViewSet(ModelViewSet):
    serializer_class = BudgetsSerializer
    queryset = BudgetsSerializer.Meta.model.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Provider guardado con exito... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
