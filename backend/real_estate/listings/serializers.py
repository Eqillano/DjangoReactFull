from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'title','address','city','price','sale_type','home_type','bedrooms','bathrooms','photo_main','slug','sqft'
        ]

class ListingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_fields = 'slug'