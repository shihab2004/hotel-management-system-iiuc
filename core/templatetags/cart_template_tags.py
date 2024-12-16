from django import template

register = template.Library()


@register.filter
def cart_item_count(user):

    return 0
