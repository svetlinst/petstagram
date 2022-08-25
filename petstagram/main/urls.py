from django.urls import path

from petstagram.main.views import show_index, show_dashboard, show_profile_details, show_photo_details

urlpatterns = [
    path('', show_index, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile_details, name='profile_details'),
    path('photo/details/<int:pk>', show_photo_details, name='photo-details')
]
