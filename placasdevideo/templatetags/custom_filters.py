from babel.numbers import format_number
from django import template

register = template.Library()


@register.filter(name='format_price')
def format_price(value):
    return format_number(value, locale='pt_BR')
