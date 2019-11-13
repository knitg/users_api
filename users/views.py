from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import UserSerializer,CustomerSerializer, MaggamDesignerSerializer,FashionDesignerSerializer, TailorSerializer, BoutiqueSerializer, AddressSerializer, ImageSerializer, MasterSerializer, UserTypeSerializer
from .models import User, Customer, MaggamDesigner,FashionDesigner, Address, Boutique, Tailor, File, Master, UserType
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = ImageSerializer
    
    def create(self, request, *args, **kwargs):
        image_serializer = ImageSerializer(data=request.data)
        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

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
    parser_classes = (MultiPartParser, FormParser,)

class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer