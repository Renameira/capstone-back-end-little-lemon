from django.shortcuts import render
from rest_framework import generics
from .models import MenuItens, Booking
from django.contrib.auth.models import User
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItens.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(
                        generics.RetrieveUpdateAPIView,
                        generics.DestroyAPIView
                        ):
    queryset = MenuItens.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message": "This view is protected"})
