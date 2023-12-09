from rest_framework import serializers
from DocUserApp.models import Doc, User, Company

class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):      
    class Meta: 
        model = User
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):  
    class Meta: 
        model = Company
        fields = '__all__'
