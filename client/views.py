from rest_framework import viewsets
from rest_framework.response import Response
from client.models import Client
from client.serializers import ClientSerializer, ClientDetailSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
class ClientAPIView(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        created_by = User.objects.first()
        serializer = ClientSerializer(data=request.data)
        request.data.update({'created_by':created_by.id})
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED, data={'message':'Client Created Successfully'})
        return Response(status=HTTP_400_BAD_REQUEST, data=serializer.errors)

    def list(self, request, *args, **kwargs):
        clients_list = Client.objects.all()
        serializer = ClientSerializer(clients_list, many=True)
        return Response(status=HTTP_200_OK, data=serializer.data)

    def get_detail(self, request, pk, *args, **kwargs):
        client = get_object_or_404(Client, id=pk)
        serializer = ClientDetailSerializer(client)
        return Response(status=HTTP_200_OK, data=serializer.data)

    def update(self, request, pk, *args, **kwargs):
        client = get_object_or_404(Client, id=pk)
        serializer = ClientSerializer(instance=client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED, data={'message':'Client Created Successfully'})
        return Response(status=HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        Client.objects.filter(id=pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)