from rest_framework import serializers
from .models import MenuItem, Booking
from django.contrib.auth.models import User, Group

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'username', 'email', 'first_name', 'last_name', 'is_superuser','is_staff','is_active','date_joined', ]
        