from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from .views import *

urlpatterns = [
    path('review/', get_create_feedback),
    path('review/<int:pk>/', get_edit_delete_feedback),
    path('logout/', logout),
    path('movies/', get_create_films),
    path('movies/<int:pk>/', get_edit_delete_films),
    path('cat/', get_create_category),
    path('cat/<int:pk>/', get_edit_delete_category),
    path('actors/', get_create_actors),
    path('actors/<int:pk>/', get_edit_delete_actors),
    path('login/', obtain_auth_token)
]