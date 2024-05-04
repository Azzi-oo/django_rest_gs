from django.urls import path
from quicstarter import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from quicstarter.views import SnippetViewSet, UserViewSet


# urlpatterns = format_suffix_patterns(urlpatterns)

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('users/', user_list, name='snippet-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    # path('snippet/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    # path('', views.api_root),
    # path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]
