from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['image','mobile_no','user']

# class PatientSerializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = Patient
#         fields = ['image','mobile_no','user']
#     def save(self ):
#         image = self.validated_data['image']
#         mobile_no = self.validated_data['mobile_no']
#         # request = self.context.get('request', None)
#         # if request:
#         #     user = request.user
#         Patient.objects.create(
#             user = self.request.user,
#             mobile_no = mobile_no,
#             image = image,
#         )

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error':"Two password field dosen't matched..!"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"Email already exist..!"})
        
        acc = User(username=username,first_name=first_name,last_name=last_name,email=email)
        acc.is_active = False
        acc.set_password(password)
        acc.save()
        return acc

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)