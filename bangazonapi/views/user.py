"""View module for handling requests about Users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import User


class UserView(ViewSet):
    """Bangazon User View"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for Single User
        Returns:
            Response -- JSON serialized User
        """
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized User instance
        """

        user = User.objects.create(
            name=request.data["name"],
            bio=request.data["bio"],
            image=request.data["image"],
            isseller=request.data["isseller"],
            uid=request.data["uid"],
        )
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a user

        Returns:
        Response -- Empty body with 204 status code
        """

        user = User.objects.get(pk=pk)
        user.name = request.data["name"]
        user.bio = request.data["bio"]
        user.image = request.data["image"]
        user.isseller = request.data["isseller"]
        user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """Delete User
        """
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserSerializer(serializers.ModelSerializer):
    """JSON Serializer For Users"""
    class Meta:
        model = User
        fields = ('id', 'name', 'bio', 'image', 'isseller', 'uid')
        depth = 1
