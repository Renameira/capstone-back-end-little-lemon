from .models import MenuItens, Booking
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class MenuSerializer(ModelSerializer):
    class Meta:
        model = MenuItens
        fields = ['title', 'price']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups',
                  'is_superuser', 'date_joined',
                  'last_login']


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
