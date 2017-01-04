from api.models import Item, Review
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    #kind = serializers.StringRelatedField() 

    class Meta:
        model = Item
        fields = ('id', 'title', 'rating', 'poster_src', 'release_date', 'kind')

class ReviewSerializer(serializers.ModelSerializer):
    #kind = serializers.StringRelatedField() 
    #item = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ('id', 'text_1', 'text_2', 'text_3', 'publish_date', 'item') 
