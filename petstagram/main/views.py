from django.shortcuts import render, redirect

from petstagram.main.models import Profile, PetPhoto


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


def show_index(request):
    return render(request, 'home_page.html')


def show_dashboard(request):
    profile = get_profile()
    pet_photos = set(PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile))
    context = {
        'pet_photos': pet_photos,
    }

    return render(request, 'dashboard.html', context)


def show_profile_details(request):
    return render(request, 'profile_details.html')


def show_photo_details(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo-details', pk)
