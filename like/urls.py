from django.urls import path, include

from .views import like, dislike

urlpatterns = [
    path('<slug:slug>/like', like, name='like'),
    path('<slug:slug>/dislike', dislike, name='dislike'),
]
