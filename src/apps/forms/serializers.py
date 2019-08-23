from rest_framework import serializers

from .models import Form

class FormDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Form
        fields = '__all__'

class FormListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
