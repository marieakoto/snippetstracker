
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializer import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions     #Allows to create and use REST permissions.
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.permissions import IsOwnerOrReadOnly


# Create your views here
class LandingPageView(APIView):
    def get(self, request):
        return Response({"message": "Welcome"})    ##The landing page view that displays whem the server is run

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  ##Sets this view to restrict access to authenticated users, and gives read only access to non authenticated  

    def perform_create(self, serializer):   ##a function to override the perform create function to allow us to modift how the instance is saved.
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]   ##same permissions is employed for these view 


##Add more views to view and retrieve user information
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

