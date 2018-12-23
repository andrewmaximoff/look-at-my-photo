from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import Http404

from .models import Like
from post.models import Post


@login_required
def like(request, *args, **kwargs):
    try:
        user = request.user
        post = Post.objects.get(slug=kwargs['slug'])
        like_relations = Like.objects.filter(content_type=ContentType.objects.get_for_model(post),
                                             object_id=post.id,
                                             user=user)

        if not like_relations.exists():
            like_relations = Like.objects.create(content_type=ContentType.objects.get_for_model(post),
                                                 object_id=post.id,
                                                 user=user)
            like_relations.save()
        return HttpResponseRedirect(
            reverse_lazy(
                'post detail',
                kwargs={'slug': kwargs['slug']}
            )
        )
    except ObjectDoesNotExist:
        raise Http404


@login_required
def dislike(request, *args, **kwargs):
    try:
        user = request.user
        post = Post.objects.get(slug=kwargs['slug'])
        like_relations = Like.objects.filter(content_type=ContentType.objects.get_for_model(post),
                                             object_id=post.id,
                                             user=user)

        if like_relations.exists():
            like_relations.delete()
        return HttpResponseRedirect(
            reverse_lazy(
                'post detail',
                kwargs={'slug': kwargs['slug']}
            )
        )
    except ObjectDoesNotExist:
        raise Http404
