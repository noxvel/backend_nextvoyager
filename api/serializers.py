from api.models import Item, Review
from rest_framework import serializers
from django.contrib.auth.models import User


class ItemSerializer(serializers.ModelSerializer):
    poster_src = serializers.ImageField(allow_empty_file=True,read_only=True) 

    class Meta:
        model = Item
        fields = ('id', 'title', 'rating', 'poster_src', 'release_date', 'kind')

class ReviewSerializer(serializers.ModelSerializer):
    #kind = serializers.StringRelatedField() 
    #item = serializers.StringRelatedField()
    #user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user = serializers.SlugRelatedField(
        queryset = User.objects.all(),
        slug_field='username'
     )
     
    class Meta:
        model = Review
        fields = ('id', 'text_1', 'text_2', 'text_3', 'publish_date', 'item', 'user') 
        #depth = 1
#    def create(self, validated_data):
 #       username = validated_data.pop('user')
  #      user = User.objects.filter(username=username)
   #     return Review.objects.create(user=user, **validated_data)

class UserSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'reviews')