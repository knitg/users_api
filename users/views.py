from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer, MaggamDesignerSerializer,FashionDesignerSerializer, TailorSerializer, BoutiqueSerializer, AddressSerializer
from .models import Customer, MaggamDesigner,FashionDesigner, Address, Boutique, Tailor

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class MaggamDesignerViewSet(viewsets.ModelViewSet):
    queryset = MaggamDesigner.objects.all()
    serializer_class = MaggamDesignerSerializer

class FashionDesignerViewSet(viewsets.ModelViewSet):
    queryset = FashionDesigner.objects.all()
    serializer_class = FashionDesignerSerializer

class BoutiqueViewSet(viewsets.ModelViewSet):
    queryset = Boutique.objects.all()
    serializer_class = BoutiqueSerializer

class TailorViewSet(viewsets.ModelViewSet):
    queryset = Tailor.objects.all()
    serializer_class = TailorSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer