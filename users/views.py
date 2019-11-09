from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import UserSerializer,CustomerSerializer, MaggamDesignerSerializer,FashionDesignerSerializer, TailorSerializer, BoutiqueSerializer, AddressSerializer, ImageSerializer
from .models import User, Customer, MaggamDesigner,FashionDesigner, Address, Boutique, Tailor, MyFile

# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):    
    queryset = MyFile.objects.all()
    serializer_class = ImageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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