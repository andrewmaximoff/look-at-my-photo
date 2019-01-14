from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile
from LookAtMyPhoto.post.models import Post


class ProfileAdmin(admin.ModelAdmin):
    pass


class UserPostInline(admin.TabularInline):
    model = Post
    extra = 1


class CustomUserAdmin(UserAdmin):
    inlines = [UserPostInline]


admin.site.register([Profile], ProfileAdmin)
admin.site.register([User], CustomUserAdmin)
