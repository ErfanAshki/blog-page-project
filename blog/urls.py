from django.urls import path

from .views import post_list_view

urlpatterns = [
    path('list/', post_list_view, name='post_list'),

]
