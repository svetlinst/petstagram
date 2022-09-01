from django.contrib import admin

from petstagram.main.models import Profile, Pet, PetPhoto


class PetInlineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    inlines = (PetInlineAdmin,)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
