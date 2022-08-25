from django.shortcuts import render


def show_index(request):
    return render(request, 'home_page.html')


def show_dashboard(request):
    return render(request, 'dashboard.html')


def show_profile_details(request):
    return render(request, 'profile_details.html')


def show_photo_details(request, pk):
    return render(request, 'profile_details.html', pk)
