
from rest_framework import serializers
from .models import Blog, Category

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    
    def retrive(self, request, *args, **kwargs):
        pass


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


