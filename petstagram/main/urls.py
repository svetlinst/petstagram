from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from petstagram.main.views import show_index, show_dashboard, show_profile_details, show_photo_details, like_pet_photo

urlpatterns = [
    path('', show_index, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile_details, name='profile-details'),
    path('photo/details/<int:pk>/', show_photo_details, name='photo-details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like-pet-photo'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
