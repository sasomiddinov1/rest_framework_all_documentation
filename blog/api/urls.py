from blog.api.views import (
    api_detail_blog_view,
    api_update_blog_view,
    api_delete_blog_view,
    api_create_blog_view,
    ApiBlogListView
)
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('<slug>/', api_detail_blog_view, name='detail'),
    path('<slug>/edit', api_update_blog_view, name='edit'),
    path('<slug>/delete', api_delete_blog_view, name='delete'),
    path('create', api_create_blog_view, name='create'),
    path('list', ApiBlogListView.as_view(), name='list'),

]