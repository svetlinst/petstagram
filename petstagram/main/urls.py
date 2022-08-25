from django.urls import path

from petstagram.main import views

urlpatterns = [
    path('', views.index)
]