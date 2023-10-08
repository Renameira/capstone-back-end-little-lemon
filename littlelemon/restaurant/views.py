from django.shortcuts import render
from rest_framework import generics
from .models import MenuItens, Booking
from django.contrib.auth.models import User
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItens.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(
                        generics.RetrieveUpdateAPIView,
                        generics.DestroyAPIView
                        ):
    queryset = MenuItens.objects.all()
    serializer_class = MenuSerializer


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
