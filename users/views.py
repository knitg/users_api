from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import UserSerializer,CustomerSerializer, MaggamDesignerSerializer,FashionDesignerSerializer, TailorSerializer, BoutiqueSerializer, AddressSerializer, ImageSerializer, MasterSerializer, UserTypeSerializer
from .models import User, Customer, MaggamDesigner,FashionDesigner, Address, Boutique, Tailor, File, Master, UserType
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework.parsers import FileUploadParser
from django.http import JsonResponse

class ImageViewSet(viewsets.ModelViewSet):
    # parser_class = (FileUploadParser,)
    queryset = File.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (FormParser, MultiPartParser, FileUploadParser) # set parsers if not set in settings. Edited

    
    def create(self, request, *args, **kwargs):
        images_arr = []
        for image in request.FILES:
            image_serializer = ImageSerializer(data= {'description': request.data['description'], 'image': request.FILES[image]})
            if image_serializer.is_valid():
                image_serializer.save()
                images_arr.append(image_serializer.instance.id)
            else:
                return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'image_ids': images_arr}, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (FormParser, MultiPartParser, FileUploadParser) # set parsers if not set in settings. Edited

    def create(self, request, *args, **kwargs):
        images_arr = []
        request.data['images'] = request.FILES
        request.data['user_type'] = int(request.data['user_type'])

        user_serializer = UserSerializer(data= request.data, context={'request': request})
        if user_serializer.is_valid():
                user_serializer.save()
        
        return Response({'userId':user_serializer.instance.id}, status=status.HTTP_201_CREATED)

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