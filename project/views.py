from rest_framework import viewsets
from rest_framework.response import Response
from project.models import Project
from project.serializers import ProjectSerializer, ProjectDetailSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from client.models import Client

# Create your views here.
class ProjectAPIView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, pk, *args, **kwargs):
        client = get_object_or_404(Client, id=pk)
        serializer = ProjectDetailSerializer(data=request.data)
        created_by = User.objects.first()
        request.data.update({'created_by': created_by.id, 'client': client.id})
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED, data={'message':'Project Created Successfully'})
        return Response(status=HTTP_400_BAD_REQUEST, data=serializer.errors)

    def list(self, request, *args, **kwargs):
        projects = Project.objects.filter(assigned_users__in = [request.user])
        serializer = ProjectSerializer(projects, many=True)
        return Response(status=HTTP_200_OK, data=serializer.data)