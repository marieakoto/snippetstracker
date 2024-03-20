

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns ##this appends the urls we will be using to accept suffix patterns
from snippets import views

urlpatterns =[
    path('', views.LandingPageView.as_view()),  ##Created landing page for 127... to see the first page there
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/' ,views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),       ##add the new views defined in view.py
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns) #Declaration that all urlpatterns should be formatted by the suffix patterns.