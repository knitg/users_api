from rest_framework import serializers
from .models import User, Customer, Tailor, MaggamDesigner, FashionDesigner, Boutique, Address, File, Master, UserType

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('image','description')

    def create(self, validated_data):
        mydata = validated_data
        return File.objects.create(**validated_data)

class UserTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserType
        fields = "__all__"

    def create(self, validated_data):       
        ## Role data 
        userType = UserType.objects.create(**validated_data)
        return userType
    
class UserSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=False)
    class Meta:
        model = User
        fields = ('userName', 'email', 'phone', 'password', 'user_type', 'user_role', 'images')
        # fields = '__all__'
    def create(self, validated_data):
        ## Image data 
        image_data = validated_data.pop('images')
        images = File.objects.create(**image_data)
        images.save()

        user = User.objects.create_user(images=images, **validated_data)
        user.save()
        return user
     


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Customer
        fields = [ 'name','user', 'address']
 
    def create(self, validated_data):
        ## User data 
        users_data = validated_data.pop('user')        
        if (users_data['user_type'] != 'CUSTOMER'):
            raise ValueError('User type should be CUSTOMER')
            return
        image_data = users_data.pop('images')
        images = File.objects.create(**image_data)
        images.save()

        user = User.objects.create_user(images=images, **users_data)
        user.save()

        ## Customer data 
        customer = Customer.objects.create(user=user, **validated_data)
        return customer

class TailorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False)    
    class Meta:
        model = Tailor
        # fields = [ 'name','user', 'address']
        fields = "__all__"

    def create(self, validated_data):       
        ## User data 
        users_data = validated_data.pop('user')        
        if (users_data['user_type'] != 'TAILOR'):
            raise ValueError('User type should be TAILOR')
            return
        image_data = users_data.pop('images')
        images = File.objects.create(**image_data)
        images.save()

        user = User.objects.create_user(images=images, **users_data)
        user.save()
        ## Tailor data 
        tailor = Tailor.objects.create(user=user, **validated_data)
        return tailor
    


class MaggamDesignerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = MaggamDesigner 
        fields = [ 'name','user', 'address']

    
    def create(self, validated_data):
        ## User data 
        users_data = validated_data.pop('user')        
        if (users_data['user_type'] != 'MAGGAM_DESIGNER'):
            raise ValueError('User type should be MAGGAM DESIGNER')
            return
        image_data = users_data.pop('images')
        images = File.objects.create(**image_data)
        images.save()

        user = User.objects.create_user(images=images, **users_data)
        user.save()

        ## MaggamDesigner data 
        maggam_designer = MaggamDesigner.objects.create(user=user, **validated_data)
        return maggam_designer


class FashionDesignerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False) 
    class Meta:
        model = FashionDesigner        
        # fields = ['user','name', 'address']
        fields = [ 'name','user', 'address']
    
    def create(self, validated_data):        
        ## User data 
        users_data = validated_data.pop('user')        
        if (users_data['user_type'] != 'FASHION_DESIGNER'):
            raise ValueError('User type should be FASHION DESIGNER')
            return
        image_data = users_data.pop('images')
        images = File.objects.create(**image_data)
        images.save()

        user = User.objects.create_user(images=images, **users_data)
        user.save()

        ## FashionDesigner data 
        fashion_designer = FashionDesigner.objects.create(user=user, **validated_data)
        return fashion_designer

class BoutiqueSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False) 
    class Meta:
        model = Boutique
        # fields = ['user','name', 'address']
        fields = [ 'name','user', 'address']

    def create(self, validated_data):
        ## User data 
        users_data = validated_data.pop('user')        
        if (users_data['user_type'] != 'BOUTIQUE'):
            raise ValueError('User type should be BOUTIQUE')
            return
        image_data = users_data.pop('images')
        images = File.objects.create(**image_data)
        images.save()

        user = User.objects.create_user(images=images, **users_data)
        user.save()

        ## Boutique data 
        boutique = Boutique.objects.create(user=user, **validated_data)
        return boutique

class MasterSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False) 
    class Meta:
        model = Master
        # fields = ['user','name', 'address']
        fields = [ 'name','user', 'address']

    def create(self, validated_data):
        ## User data 
        users_data = validated_data.pop('user')        
        if (users_data['user_type'] != 'BOUTIQUE'):
            raise ValueError('User type should be BOUTIQUE')
            return
        image_data = users_data.pop('images')
        images = File.objects.create(**image_data)
        images.save()

        user = User.objects.create_user(images=images, **users_data)
        user.save()

        ## MASTER data 
        master = Master.objects.create(user=user, **validated_data)
        return master

        
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address_line_1', 'address_line_2', 'url', 
        'landmark', 'postalCode', 'latitude', 'longitude',
        'geoAddress', 'city', 'state', 'created_at', 'updated_at'
        ]

