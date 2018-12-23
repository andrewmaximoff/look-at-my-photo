from django.urls import path, include

from .views import follow, unfollow, UserUpdateView


urlpatterns = [
    path('', include('allauth.urls')),
    path('follow/<slug:slug>/follow', follow, name='follow'),
    path('follow/<slug:slug>/unfollow', unfollow, name='unfollow'),
    path('edit-profile/<slug:slug>/', UserUpdateView.as_view(), name='edit profile'),
    path('edit-profile/<slug:slug>/', UserUpdateView.as_view(), name='edit profile'),
]
