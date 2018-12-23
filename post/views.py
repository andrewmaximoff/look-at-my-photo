from django.contrib.auth import get_user_model
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView, MultipleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from accounts.models import Follower
from .models import Post

User = get_user_model()


class UserDetailView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'post/user-detail.html'
    slug_field = "username"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        object_list = self.object.post_set.all().order_by('-pub_time')
        context = super(UserDetailView, self).get_context_data(object_list=object_list, **kwargs)
        if self.request.user.is_authenticated and \
                Follower.objects.filter(
                    follower=self.request.user,
                    following=context['object']
                ).exists():
            context['follow'] = True
        else:
            context['follow'] = False
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'


class FeedListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'post/feed-list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            following = user.following.values_list('following_id', flat=True)
            posts = self.model.objects.filter(user_id__in=following)
            return posts.order_by('-pub_time')

        return self.model.objects.order_by('-pub_time')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'description']
    template_name = 'post/post-create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('post detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

