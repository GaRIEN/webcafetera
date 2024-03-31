from django import template
from ..models import Paginas

register = template.Library()

@register.simple_tag
def get_paginas():
    return Paginas.objects.all()
