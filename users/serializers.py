from rest_framework import serializers
from .models import Customer, Tailor, Designer, Boutique, Address

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'fullName', 'userName', 'email', 'mobileNo',
        'address', 'created_at', 'updated_at'
        ]


class TailorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tailor
        fields = ['id', 'fullName', 'shopName','userName', 'email', 'mobileNo',
        'address', 'created_at', 'updated_at'
        ]


class DesignerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Designer        
        fields = ['id', 'fullName', 'shopName','userName', 'email', 'mobileNo',
        'address', 'created_at', 'updated_at'
        ]

class BoutiqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boutique
        fields = ['id', 'fullName', 'shopName','userName', 'email', 'mobileNo',
        'address', 'created_at', 'updated_at'
        ]

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address_line_1', 'address_line_2', 'url', 
        'landmark', 'postalCode', 'latitude', 'longitude',
        'geoAddress', 'city', 'state', 'created_at', 'updated_at'
        ]


