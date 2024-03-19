from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializer import SnippetSerializer


# Create your views here

@api_view(['GET', 'POST'])  ##wraps functions in api view and declares the httpresponse
def snippet_list(request, format = None): #specifiying that theapi will handle urls in either json or api format
    ### Lists all code snippets or create a new snippet.

    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many = True)
        return Response(serializer.data) 
    
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)  ##Responds with http status 202, we define the status here
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST) ##Responds with status as well , but we define the exact status to display
    

@api_view(['GET', 'PUT', 'DELETE']) ##Wraps api in an api view to get the right responses. Must declare the responses to be worked with.
def snippet_detail(request,pk, format = None): #api will handle urls in either json or api format
    ### Retrieve, update or delete a code snippet.

    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    