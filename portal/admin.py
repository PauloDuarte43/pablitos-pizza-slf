# -*- coding: utf-8 -*-
from django.contrib import admin

from models import Ingredient, Pizza, PizzaIngredient, Schedules


class PizzaIngredientInline(admin.TabularInline):
    model = PizzaIngredient
    extra = 1

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'show_ingredients')
    #filter_horizontal = ('ingredients',)
    inlines = (PizzaIngredientInline,)
    ordering = ('code',)
    def show_ingredients(self, obj):
        #return dir(obj)
        return ", ".join([a.name for a in obj.ingredients.all()])


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'priority')
    ordering = ('name',)


class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('day_week', 'from_hour', 'to_hour')


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Schedules, SchedulesAdmin)
