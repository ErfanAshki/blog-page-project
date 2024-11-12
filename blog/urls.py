from django.urls import path

from .views import post_list_view, post_detail_view, post_create_view, post_update_view

urlpatterns = [
    path('list/', post_list_view, name='post_list'),
    path('<int:pk>/', post_detail_view, name='post_detail'),
    path('create/', post_create_view, name='post_create'),
    path('<int:pk>/update/', post_update_view, name='post_update'),

]
