# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 20:23:02 2022

@author: Sujay
"""

from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}