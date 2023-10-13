from rest_framework import serializers
from .models import cab,Hotels,lodge,places,food
class apicab(serializers.ModelSerializer):
    class Meta:
        model=cab
        fields=('driver_name','vechile_no','phone_no1','phone_no2')
        
class apiHotels(serializers.ModelSerializer):
    class Meta:
        model=Hotels
        fields=('location','type','image','name','number','rating')
        
class apiplaces(serializers.ModelSerializer):
    class Meta:
        model=places
        fields=('place_name','place_desc','location')
        
class apilodge(serializers.ModelSerializer):
    class Meta:
        model=lodge
        fields=('name','contacts','address','typeOfroom','total_rooms')
class apifood(serializers.ModelSerializer):
    class Meta:
        model=food
        fields='__all__'
        