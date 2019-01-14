from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import Http404

from .models import User, Follower, Profile


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['avatar', 'bio']
    slug_field = "user__username"
    template_name = 'post/user-update.html'

    def get_success_url(self, **kwargs):
        self.object.refresh_from_db()
        return reverse_lazy('user detail', kwargs={'slug': self.object.user.username})

    def form_valid(self, form):
        form.instance.user = self.request.user
        import pprint
        pprint.pprint(form.data)
        pprint.pprint(type(form.non_field_errors))
        if (User.objects.filter(username=form.data['username']).exists() and
                self.request.user.username != form.data['username']):
            form.add_error(None, 'This username isn\'t available. Please try another.')
            return self.form_invalid(form)
        else:
            User.objects.filter(profile=self.object).update(username=form.data['username'])
        return super().form_valid(form)


@login_required
def follow(request, *args, **kwargs):
    try:
        follower = request.user
        following = User.objects.get(username=kwargs['slug'])
        follow_relations = Follower.objects.filter(follower=follower, following=following)

        if not follow_relations.exists():
            follow_relations = Follower.objects.create(follower=follower, following=following)
            follow_relations.save()

        return HttpResponseRedirect(
            reverse_lazy(
                'user detail',
                kwargs={'slug': kwargs['slug']}
            )
        )
    except User.DoesNotExist:
        raise Http404


@login_required
def unfollow(request, *args, **kwargs):
    try:
        follower = request.user
        following = User.objects.get(username=kwargs['slug'])
        follow_relations = Follower.objects.filter(follower=follower, following=following)

        if follow_relations.exists():
            follow_relations.delete()

        return HttpResponseRedirect(
            reverse_lazy(
                'user detail',
                kwargs={'slug': kwargs['slug']}
            )
        )
    except User.DoesNotExist:
        raise Http404
