from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields=['username','email','password','password2']
        extra_kwargs= {
            'password':{'write_only':True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email = self.validated_data['email']
        if password != password2:
            raise serializers.ValidationError({'Error':"password 1 and 2 do not match"})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'Error':'email already exist in database'})
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'Error':'username already exist in database'})
        account = User(email=email,username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)