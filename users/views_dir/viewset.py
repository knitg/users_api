from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from users.serializers import CustomerSerializer, AddressSerializer
from users.models import Customer, Address

# Create your views here.
class Customer1ViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # @action(detail= True, method=['post'])
    # def set_created_date(self, request, pk=None):
    #     customer = self.get_object()

