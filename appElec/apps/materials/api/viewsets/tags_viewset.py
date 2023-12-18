from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..serializer.tag_serializer import TagsSerializer

class TagsViewSet(ModelViewSet):
    serializer_class = TagsSerializer
    queryset = TagsSerializer.Meta.model.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Tag guardado con exito... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)