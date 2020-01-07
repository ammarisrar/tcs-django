from django.urls import path

from . import views

urlpatterns = [
    path('', views.viewpage, name='view_homepage'),
]