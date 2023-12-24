from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializer import MessageSerializer, MobileTokenSerializer


class MessageViewSet(GenericViewSet):
    serializer_class = MessageSerializer
    queryset = MessageSerializer.Meta.model.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        item = self.get_object()
        serializer = self.get_serializer(instance=item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "message update... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MobileTokenViewSet(GenericViewSet):
    serializer_class = MobileTokenSerializer
    queryset = MobileTokenSerializer.Meta.model.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()
            id = instance.id
            return Response(
                {"id": id, "message": "Token guardado con exito... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        item = self.get_object()
        serializer = self.get_serializer(instance=item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "message update... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
