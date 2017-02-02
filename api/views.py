from api.models import Item, Review
from api.serializers import ItemSerializer, ReviewSerializer, UserSerializer
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework import permissions

class ItemList(APIView):
    """
    List all items, or create a new item.
    """

    def get(self,request, kind, format=None):
        items = Item.objects.filter(kind__name=kind)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self,request, kind, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetail(APIView):
    """
    Retrieve, update or delete a code item
    """

    def get_object(self, pk):
        try:
           return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404 

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################# Review ###########

class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_pk']
        return Review.objects.filter(item__id=item_id)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

##################### User ###############
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticated,)
