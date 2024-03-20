

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns ##this appends the urls we will be using to accept suffix patterns
from snippets import views


#must name paths when using hyperlinked apis
urlpatterns =[
    #path('', views.LandingPageView.as_view()),  ##Created landing page for 127... to see the first page there :used this as lsnding page but not anymmore
    path('', views.api_root),       #pattern for the api_root view created.
    path('snippets/', views.SnippetList.as_view() ,name = 'snippet-list'),
    path('snippets/<int:pk>/' ,views.SnippetDetail.as_view() , name = 'snippet-detail'),
    path('users/', views.UserList.as_view(), name = 'user-list'),       ##added the new user views defined in view.py
    path('users/<int:pk>/', views.UserDetail.as_view(), name = 'user-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name= 'snippet-highlight'),      ##New view for the highlighted snippets api
]

urlpatterns = format_suffix_patterns(urlpatterns) #Declaration that all urlpatterns should be formatted by the suffix patterns.