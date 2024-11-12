from django.urls import path

from .views import PostListView, PostDetailView, post_create_view, post_update_view, post_delete_view

urlpatterns = [
    path('list/', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', post_create_view, name='post_create'),
    path('<int:pk>/update/', post_update_view, name='post_update'),
    path('<int:pk>/delete/', post_delete_view, name='post_delete'),

]
