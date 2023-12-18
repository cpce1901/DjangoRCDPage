from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..serializer.provider_serializer import ProvidersSerializer

class ProviderViewSet(ModelViewSet):
    serializer_class = ProvidersSerializer
    queryset = ProvidersSerializer.Meta.model.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Provider guardado con exito... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)