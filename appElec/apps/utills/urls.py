from django.urls import path
from .views import CapacitorApiView

app_name = "utills_app"

urlpatterns = [
    path("capacitor/trifasico/<float:kw>/<float:fp>/<float:fp_need>/", CapacitorApiView.as_view(), name="capacitor-trifasico"),

]