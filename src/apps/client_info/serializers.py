from rest_framework import serializers

from .models import *


class ExtUserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_id(obj):
        return obj.ext_id

    class Meta:
        model = ExtUser
        fields = ('id', 'name', 'username', 'email')


class ExtTariffSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_id(obj):
        return obj.ext_id

    class Meta:
        model = ExtTariff
        fields = ('id', 'name', 'size', 'websites', 'databases')


class ClientInfoReadSerializer(serializers.ModelSerializer):
    client = ExtUserSerializer(read_only=True)
    tariff = ExtTariffSerializer(read_only=True)

    class Meta:
        model = ClientInfo
        fields = ('id', 'status', 'success', 'client', 'tariff')


class ClientInfoPostSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    tariff_id = serializers.IntegerField()
