from ..serializer.tag_serializer import TagsSerializer
from appElec.api import GeneralListApiView


class TagsListApi(GeneralListApiView):
    serializer_class = TagsSerializer
