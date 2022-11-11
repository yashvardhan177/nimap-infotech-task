from rest_framework import serializers
from client.models import Client
from project.serializers import ProjectSerializer

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ['id', 'name', 'created_at', 'updated_at', 'created_by']

class ClientDetailSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(source='project_client', many=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'created_at', 'updated_at', 'created_by', 'projects']