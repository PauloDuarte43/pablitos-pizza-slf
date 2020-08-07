# -*- coding: utf-8 -*-
from django import template

from portal.models import PizzaIngredient

register = template.Library()


@register.filter
def orderingredient(value):
    ingredients = []
    for i in PizzaIngredient.objects.filter(pizza=value):
        ingredients.append(i.ingredient)
    return ingredients
