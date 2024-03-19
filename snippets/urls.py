

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns ##this appends the urls we will be using to accept suffix patterns
from snippets import views

urlpatterns =[
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/' ,views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns) #Declaration that all urlpatterns should be formatted by the suffix patterns.