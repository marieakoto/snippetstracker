from django.urls import path,include
from rest_framework.routers import DefaultRouter
from snippets import views

router = DefaultRouter()    #must define default router for urls. this automatically includes an api root.
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  ##Includes the login and logout views for the API
]
