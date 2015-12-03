from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    user_token = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = Device
        fields = ('id', 'owner', 'ip', 'status', 'connected', 'user_token')
        read_only_fields = ('id', 'owner', 'status', 'connected')

    def create(self, validated_data):
        validated_data.pop('user_token', None)
        return Device.objects.create(**validated_data)