from rest_framework import generics
from .models import Location, Item
from .serializers import LocationSerializer, ItemSerializer


# Create your views here.
# this read and write endpoint is using to create items for our API provides the get & post handlers
class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    # queryset function is used to get data from database
    def get_queryset(self):
        queryset = Item.objects.all()
        # when the ItemList API view is called we have access to request object
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemLocation=location)
        return queryset


# this detail view is used to read, update, delete
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
