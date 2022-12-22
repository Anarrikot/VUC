from rest_framework import serializers

from .models import Solder

class SolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solder
        fields = '__all__'

class SolderDetailSerializer(serializers.ModelSerializer):
    title_name = serializers.SerializerMethodField()
    class Meta:
        model = Solder
        fields = '__all__'
    def get_title_name(self, obj):
        return f'{obj.title.name}'

