
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializer import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions     #Allows to create and use REST permissions.
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view      #To implement the apiview in our function based view
from rest_framework.reverse import reverse   
from rest_framework import renderers


##Function based view to create single entry point to our API:
@api_view(['GET'])
def api_root(request, format = None):    #Reverse is used to return fully-qualified URLs
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request = request, format=format)
    })



# Create your views here
# class LandingPageView(APIView):
#     def get(self, request):
#         return Response({"message": "Welcome"})    ##The landing page view that displays whem the server is run.Used this landing page before api root

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  ##Sets this view to restrict access to authenticated users, and gives read only access to non authenticated  

    def perform_create(self, serializer):   ##a function to override the perform create function to allow us to modift how the instance is saved.
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]   ##Includes permissions for only owner to have write access and same permissions is employed for these view 


##Add more views to view and retrieve user information
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


##View for highlighted snippets
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self,request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)