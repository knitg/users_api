from rest_framework import serializers
from .models import User, KCustomer, KVendorUser, KAddress, KImage, KUserType

class KImageSerializer(serializers.HyperlinkedModelSerializer): 
    url = serializers.HyperlinkedIdentityField(view_name='upload-detail', source='image',)
    class Meta:
        model = KImage
        fields = ('id', 'image','description', 'url')
        # fields = '__all__'

    def create(self, validated_data):
        mydata = validated_data
        img = KImage.objects.create(**validated_data)
        return img


class KUserTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KUserType
        fields = "__all__"

    def create(self, validated_data):       
        ## Role data 
        userType = UserType.objects.create(**validated_data)
        return userType
    
class UserSerializer(serializers.ModelSerializer):
    images = KImageSerializer(many=True, required=False, allow_null=True)
    user_type = KUserTypeSerializer(many=True, required=False, allow_null=True) 
    class Meta:
        model = User
        fields = ('url', 'userName', 'email', 'phone', 'password', 'user_type', 'user_role', 'images')
         

    def create(self, validated_data):
        ## Image data 
        user = User.objects.create_user(**validated_data)
        user.save()

        if self.initial_data.get('images'):
            validated_data['images'] = self.initial_data['images']
            image_data = validated_data.pop('images')
            for image in image_data:
                c_image= image_data[image]
                images = Image.objects.create(image=c_image, description=self.initial_data.get('description'), source='user_'+str(user.id), size=c_image.size)
                images.save()
                user.images.add(images)         

        # for userType in validated_data['user_type']:
        if self.initial_data.get('user_type'):
            user_types = self.initial_data['user_type'].split(',')
            usertypes = list(UserType.objects.filter(id__in=user_types))
            user.user_type.set(usertypes)

        return user

class KCustomerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = KCustomer
        fields = [ 'name','user', 'address']
 
    def create(self, validated_data):
        ## User data 
        validated_data['user'] = self.initial_data['user']
        users_data = validated_data.pop('user')
        users_data['images'] = self.initial_data['images']
        # users_data['user_type'] = self.initial_data.get('user')['user_type']
        # request.data   

        user_serializer = UserSerializer(data= users_data)
        if user_serializer.is_valid():
            user_serializer.save()
            # validated_data.pop('images')
            validated_data['name'] = 'MMMAHIIIAPPPALL'
            # validated_data['description'] = 'description here..'
            customer = KCustomer.objects.create(user=user_serializer.instance, **validated_data)
            return customer
        else:
            return user_serializer.errors
        

class KVendorUserSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False)    
    class Meta:
        model = KVendorUser
        # fields = [ 'name','user', 'address']
        fields = "__all__"

    def create(self, validated_data):       
        ## User data 
        users_data = validated_data.pop('user')        
         
        image_data = users_data.pop('images')
        images = KImage.objects.create(**image_data)
        images.save()

        kVendorUser = KVendorUser.objects.create_user(images=images, **users_data)
        kVendorUser.save()
        ## Tailor data 
        # tailor = Tailor.objects.create(user=user, **validated_data)
        # return tailor
        
class KAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KAddress
        fields = ['id', 'address_line_1', 'address_line_2', 'url', 
        'landmark', 'postalCode', 'latitude', 'longitude',
        'geoAddress', 'city', 'state', 'created_at', 'updated_at'
        ]

