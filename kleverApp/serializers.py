from django.contrib.auth.models import User
from rest_framework import serializers, validators


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    extra_kwargs = {
        'password': {
            'write_only': True,
        },
        'email': {
            'required': True,
            'unique': True,
            'allow_blank': False,
            'validators': [
                validators.UniqueValidator(
                    User.objects.all(), 'A user with that email already exists.'
                )
            ]
        }
    }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user = User.objects.create(username=username, email=email,
                                   password=password, first_name=first_name, last_name=last_name)
        return user
