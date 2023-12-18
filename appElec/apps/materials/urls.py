from django.urls import path
from .api.views.materials_view import MaterialsListApi, MaterialsCreateApi, MaterialsDetailApi, MaterialsDeleteApi, MaterialsUpdateApi

from .api.views.provider_view import ProvidersListApi


app_name = "materials_app"

urlpatterns = [
    path("materials/", MaterialsListApi.as_view(), name="materials-list"),
    path("materials/create/", MaterialsCreateApi.as_view(), name="materials-create"),
    path("materials/detail/<int:pk>/", MaterialsDetailApi.as_view(), name="materials-detail"),
    path("materials/delete/<int:pk>/", MaterialsDeleteApi.as_view(), name="materials-delete"),
    path("materials/update/<int:pk>/", MaterialsUpdateApi.as_view(), name="materials-update"),

]