from django.urls import path, include

from .views import UserDetailView, PostDetailView, FeedListView, PostCreateView

urlpatterns = [
    path('p/create/', PostCreateView.as_view(), name='post create'),
    path('<slug:slug>/', UserDetailView.as_view(), name='user detail'),
    path('p/<slug:slug>/', PostDetailView.as_view(), name='post detail'),
    path('', FeedListView.as_view(), name='feed list'),
]
