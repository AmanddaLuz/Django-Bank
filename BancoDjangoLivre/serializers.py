from rest_framework import serializers
from .models import User, Transfer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','cpf','email']
        read_only_fields = ['creation', ]


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','cpf','balance','number']
        read_only_fields = ['creation', 'balance']

