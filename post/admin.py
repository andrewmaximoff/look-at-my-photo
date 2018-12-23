from django.contrib import admin

from .models import Post


class Admin(admin.ModelAdmin):
    pass


admin.site.register(Post, Admin)
