from rest_framework import status
from rest_framework.response import Response
from ..serializer.material_serializer import MaterialsSerializer
from appElec.api import GeneralListApiView
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)


class MaterialsListApi(GeneralListApiView):
    serializer_class = MaterialsSerializer


class MaterialsCreateApi(CreateAPIView):
    serializer_class = MaterialsSerializer

    def post(self, request):

        """
        Crea un anueva instancia de un material

        params,
        tag => relacion a instancia tag INT,
        description => Descripcion del material,
        unit => recibe [0,1,2,3] INT = ["gl", "c/u", "m", "tira"],
        price => precio del material en INT,
        provider => relacion a instancia Provider INT,

        """
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Material guardado con exito"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MaterialsDetailApi(RetrieveAPIView):
    serializer_class = MaterialsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class MaterialsDeleteApi(DestroyAPIView):
    serializer_class = MaterialsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def delete(self, request, pk=None):
        material = self.get_queryset().filter(id=pk).first()

        if material:
            material.delete()
            return Response(
                {"message": "Material eliminado con exito... "},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": "No existe un material con estos datos... "},
            status=status.HTTP_400_BAD_REQUEST,
        )


class MaterialsUpdateApi(UpdateAPIView):
    serializer_class = MaterialsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def put(self, request, pk=None):
        """
        Actualiza un anueva instancia de un material

        params,
        tag => relacion a instancia tag INT,
        description => Descripcion del material,
        unit => recibe [0,1,2,3] INT = ["gl", "c/u", "m", "tira"],
        price => precio del material en INT,
        provider => relacion a instancia Provider INT,

        """
        material_serializer = self.serializer_class(
            self.get_queryset().filter(id=pk).first(), data=request.data
        )
        if material_serializer.is_valid():
            material_serializer.save()
            return Response(material_serializer.data, status=status.HTTP_200_OK)
        return Response(material_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
