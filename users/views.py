from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import UserSerializer,CustomerSerializer, MaggamDesignerSerializer,FashionDesignerSerializer, TailorSerializer, BoutiqueSerializer, AddressSerializer, ImageSerializer, MasterSerializer, UserTypeSerializer
from .models import User, Customer, MaggamDesigner,FashionDesigner, Address, Boutique, Tailor, Image, Master, UserType
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework.parsers import FileUploadParser
from django.http import JsonResponse
import json

class ImageViewSet(viewsets.ModelViewSet):
    # parser_class = (FileUploadParser,)
    queryset = Image.objects.all()
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
        if request.FILES:
            request.data['images'] = request.FILES

        user_serializer = UserSerializer(data= request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'userId':user_serializer.instance.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        ''' Save User using ajax '''
        # $("input[type='button']").on("click", function(){ 
        #     formData = new FormData();
        #     var files = $("#file")[0].files;
        #     for (var i = 0; i < files.length; i++) {
        #     var file = files[i];
        #     formData.append("image"+i, file)
            
        #     }
        #     formData.append("description", 'MAHIIIPAL2222222222');
        #     formData.append("userName", 'mahi2');
        #     formData.append("phone", 9700968447);
        #     formData.append("password", "site11");
        #     formData.append("email", 'mahi653335@gmail.com');
        #     formData.append("user_type", [1,2]); // user types
        #     formData.append("user_role", "ADMIN"); 
        #     $.ajax({
        #         url: "http://localhost:8000/api/user/", 
        #         type: 'POST',      
        #         data: formData,    
        #         cache: false,
        #         contentType: false,
        #         processData: false,
        #         success: function(returnhtml){     
        #             console.log("HELLLOOOOOE")
        #             return returnhtml;            
        #         }                 
        #     });    
        # })   
        

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    parser_classes = (FormParser, MultiPartParser, FileUploadParser) # set parsers if not set in settings. Edited

    def create(self, request, *args, **kwargs):
        # set to mutable
        request.data._mutable = True

        ## Files assigned to request data images
        request.data['images'] = []
        if request.FILES:
            request.data['images'] = request.FILES
        
        ## Files assigned to request data images
        if request.data.get('user.userName'):
            customer_serializer = CustomerSerializer(data= request.data)
        else:
            customer_serializer = CustomerSerializer(data= {'user': request.data, 'address':None, 'images':request.data['images']}, context={'request': request})
        
        ### Customer serializer save initiated
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response({'customerId':customer_serializer.instance.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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