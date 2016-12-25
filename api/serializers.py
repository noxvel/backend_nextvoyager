from api.models import Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    #type_item = serializers.HyperlinkedIdentityField(view_name='type')

    class Meta:
        model = Item
        fields = ('id','title', 'rating', 'poster_src','release_date', 'type_id')
