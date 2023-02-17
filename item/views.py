from rest_framework.generics import DestroyAPIView, ListCreateAPIView

from utils.mixins import SerializerByMethodMixin

from .models import Item
from .serializers import CreateItemSerializer, ListItemSerializer


class ListCreateitemView(SerializerByMethodMixin, ListCreateAPIView):

    queryset = Item.objects.all()

    serializer_map = {
        "GET": ListItemSerializer,
        "POST": CreateItemSerializer,
        "DELETE": CreateItemSerializer,
    }

    lookup_url_kwarg = "id_item"

class DeleteItemView(SerializerByMethodMixin, DestroyAPIView):
    
    queryset = Item.objects.all()

    serializer_map = {
        "DELETE": CreateItemSerializer,
    }

    lookup_url_kwarg = "id_item"
