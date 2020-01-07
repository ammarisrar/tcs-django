from django.urls import path

from . import views

urlpatterns = [
    path('',views.viewTrackingPage,name='tracking_page')
]