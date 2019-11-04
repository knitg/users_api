from rest_framework import serializers
from .models import User, Customer, Tailor, MaggamDesigner, FashionDesigner, Boutique, Address



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'userName',)


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'fullName', 'userName', 'email', 'mobileNo', 'password',
        'address', 'created_at', 'updated_at'
        ]


class TailorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tailor
        fields = ['id', 'fullName', 'shopName','userName', 'email', 'mobileNo','password',
        'address', 'created_at', 'updated_at'
        ]


class MaggamDesignerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaggamDesigner        
        fields = ['id', 'fullName', 'shopName','userName', 'email', 'mobileNo','password',
        'address', 'created_at', 'updated_at'
        ]

class FashionDesignerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FashionDesigner        
        fields = ['id', 'fullName', 'shopName','userName', 'email', 'mobileNo','password',
        'address', 'created_at', 'updated_at'
        ]

class BoutiqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boutique
        fields = ['id', 'fullName', 'shopName','userName', 'email', 'mobileNo','password',
        'address', 'created_at', 'updated_at'
        ]

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address_line_1', 'address_line_2', 'url', 
        'landmark', 'postalCode', 'latitude', 'longitude',
        'geoAddress', 'city', 'state', 'created_at', 'updated_at'
        ]


