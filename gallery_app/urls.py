'''Defines URL patterns for gallery_app.'''

from django.urls import path 
from . import views 

app_name = 'gallery_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_image/', views.upload_view, name= 'upload_image'),
]