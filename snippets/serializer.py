from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):  ##Moves form a modelserializer to a hyperlinked model serializer when hyperlinking our api
    owner = serializers.ReadOnlyField(source='owner.username')  #associates snippets with users that created.
    highlight = serializers.HyperlinkedIdentityField(view_name = 'snippet-highlight', format ='html')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title','code', 'linenos', 'language' , 'style']     #add url, highlight and owner fields
    
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many= True, view_name = 'snippet-detail', read_only = True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']