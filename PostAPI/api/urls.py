from .views import PostListView
from django.conf.urls import url

urlpatterns = [
    url(r'^post/$', PostListView.as_view(), name='post-list'),
]