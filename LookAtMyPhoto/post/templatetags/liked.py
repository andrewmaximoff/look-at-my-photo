from django import template

register = template.Library()


@register.filter
def is_liked(obj, username):
    return obj.likes.filter(user__username=username).exists()
