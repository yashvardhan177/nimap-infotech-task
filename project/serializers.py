from rest_framework import serializers
from project.models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id','name', 'created_at', 'created_by']
        write_only_fields = ('client')

class ProjectDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['id','name', 'created_at', 'created_by', 'assigned_users', 'client']
        write_only_fields = ('client')