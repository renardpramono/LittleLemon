from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()  # Queryset for all Menu items
    serializer_class = MenuSerializer  # Serializer to handle Menu items

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()  # Queryset for all Menu items
    serializer_class = MenuSerializer  # Serializer to handle single Menu items

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all Booking objects
    serializer_class = BookingSerializer  # Use the BookingSerializer for serialization
    permission_classes = [IsAuthenticated]