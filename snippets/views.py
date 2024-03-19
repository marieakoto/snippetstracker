from rest_framework import mixins
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializer import SnippetSerializer


# Create your views here

class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post (self, request, *args, **kwargs):
        return self.create (request, *args, **kwargs)



class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset  = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put( self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    






#####CLASS BASED VIEWS:



# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.http import Http404
# from snippets.models import Snippet
# from snippets.serializer import SnippetSerializer


# # Create your views here

# class SnippetList(APIView):                                          ## Creates a class using api view

#         ### Lists all code snippets or create a new snippet.
    
#     def get(self,request,format = None):                            #specifiying that the api will handle urls in either json or api format
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return Response(serializer.data) 
    


#     def post(self,request,format = None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)  ##Responds with the data and http status 201, we define the status here
#         return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST) ##Responds with the error and status as well , but we define the exact status to display
        



# class SnippetDetail(APIView):                            ##Wraps api in an api view to get the right responses. Must declare the responses to be worked with.
    
#         ### Retrieve, update or delete a code snippet.
       
#     def get_object(self,pk):          #api will handle urls in either json or api format
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

   
#     def get(self,request,pk,format = None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
    

#     def put(self,request,pk,format = None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk, format = None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
    









  #####FUNCTION BASED API VIEWS:

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from snippets.models import Snippet
# from snippets.serializer import SnippetSerializer


# # Create your views here

# @api_view(['GET', 'POST'])  ##wraps functions in api view and declares the httpresponse
# def snippet_list(request, format = None): #specifiying that the api will handle urls in either json or api format
#     ### Lists all code snippets or create a new snippet.

#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return Response(serializer.data) 
    
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)  ##Responds with the data and http status 201, we define the status here
#         return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST) ##Responds with the error and status as well , but we define the exact status to display
    

# @api_view(['GET', 'PUT', 'DELETE']) ##Wraps api in an api view to get the right responses. Must declare the responses to be worked with.
# def snippet_detail(request,pk, format = None): #api will handle urls in either json or api format
#     ### Retrieve, update or delete a code snippet.

#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
    