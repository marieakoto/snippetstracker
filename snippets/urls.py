

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns ##this appends the urls we will be using to accept suffix patterns
from snippets.views import  api_root,SnippetViewSet, UserViewSet
from rest_framework import renderers

##Binding the http methos to the required action for each view:

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'},
    renderer_classes = [renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get':'list'
})

user_detail = UserViewSet.as_view({
    'get' : 'retrieve'
})


#must name paths when using hyperlinked apis
urlpatterns =format_suffix_patterns[ # #Declaration that all urlpatterns should be formatted by the suffix patterns.
    #path('', views.LandingPageView.as_view()),  ##Created landing page for 127... to see the first page there :used this as lsnding page but not anymmore
    path('', api_root),       #pattern for the api_root view created.
    path('snippets/', snippet_list ,name = 'snippet-list'),
    path('snippets/<int:pk>/' ,snippet_detail , name = 'snippet-detail'),
    path('users/', user_list, name = 'user-list'),       ##added the new user views defined in view.py
    path('users/<int:pk>/', user_detail, name = 'user-detail'),
    path('snippets/<int:pk>/highlight/',snippet_highlight, name= 'snippet-highlight'),      ##New view for the highlighted snippets api
]
