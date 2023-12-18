from ..serializer.provider_serializer import ProvidersSerializer
from appElec.api import GeneralListApiView


class ProvidersListApi(GeneralListApiView):
    serializer_class = ProvidersSerializer
