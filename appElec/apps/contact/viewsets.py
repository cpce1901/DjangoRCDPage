from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import MessageSerializer


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = MessageSerializer.Meta.model.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Provider guardado con exito... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
