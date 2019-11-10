from rest_framework import serializers
from .models import User, Customer, Tailor, MaggamDesigner, FashionDesigner, Boutique, Address, File

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('image','description')

    def create(self, validated_data):
        validated_data['source'] = 'tailor'
        mydata = validated_data
        return File.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userName', 'email', 'phone', 'password', 'user_type', 'user_role')
        # fields = '__all__'
     


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Customer
        # fields = ['user','name', 'address']
        fields = "__all__"

    def create(self, validated_data):
        users_data = validated_data.pop('user')
        user = User.objects.create_user(**users_data)
        user.save()
        customer = Customer.objects.create(user=user, **validated_data)
        return customer
    


class TailorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    myfile = ImageSerializer(many=True)
    
    # user = serializers.HyperlinkedRelatedField(view_name='user',queryset=User.objects.all())
    
    class Meta:
        model = Tailor
        fields = ['myfile', 'user','name', 'address']
        # fields = "__all__"

    def create(self, validated_data):
        users_data = validated_data.pop('user')
        if (users_data['user_type'] != 'TAILOR'):
            raise ValueError('User type should be tailor')
            return
        user = User.objects.create_user(**users_data)
        user.save()
        tailor = Tailor.objects.create(user=user, **validated_data)
        return tailor
    


class MaggamDesignerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaggamDesigner 
        # fields = ['user','name', 'address']
        fields = "__all__"

    def create(self, validated_data):
        users_data = validated_data.pop('user')
        user = User.objects.create_user(**users_data)
        user.save()
        maggam_designer = MaggamDesigner.objects.create(user=user, **validated_data)
        return maggam_designer


class FashionDesignerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FashionDesigner        
        # fields = ['user','name', 'address']
        fields = "__all__"

    def create(self, validated_data):
        users_data = validated_data.pop('user')
        user = User.objects.create_user(**users_data)
        user.save()
        fashion_designer = FashionDesigner.objects.create(user=user, **validated_data)
        return fashion_designer

class BoutiqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boutique
        # fields = ['user','name', 'address']
        fields = "__all__"

    def create(self, validated_data):
        users_data = validated_data.pop('user')
        user = User.objects.create_user(**users_data)
        user.save()
        boutique = Boutique.objects.create(user=user, **validated_data)
        return boutique

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address_line_1', 'address_line_2', 'url', 
        'landmark', 'postalCode', 'latitude', 'longitude',
        'geoAddress', 'city', 'state', 'created_at', 'updated_at'
        ]

