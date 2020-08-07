# -*- coding: utf-8 -*-
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=240)
    priority = models.IntegerField(default=1)

    class Meta:
        ordering = ('priority',)

    def __unicode__(self):
        return "%s" % (self.name)


class Pizza(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient, through='PizzaIngredient')


    def ordered_ingredient(self):
        ingredients = []
        for i in PizzaIngredient.objects.filter(pizza=self):
            ingredients.append(i.ingredient)
        return ingredients

    def __unicode__(self):
        return "%s %s" % (self.code, self.name)


class PizzaIngredient(models.Model):
    pizza = models.ForeignKey(Pizza)
    ingredient = models.ForeignKey(Ingredient)
    order = models.IntegerField()

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return "%s %s" % (self.ingredient.name, self.order)

class Schedules(models.Model):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    DAY_OF_THE_WEEK = (
        (SUNDAY, 'Domingo'),
        (MONDAY, 'Segunda-feira'),
        (TUESDAY, 'Terça-feira'),
        (WEDNESDAY, 'Quarta-feira'),
        (THURSDAY, 'Quinta-feira'),
        (FRIDAY, 'Sexta-feira'),
        (SATURDAY, 'Sábado'),
    )

    day_week = models.IntegerField(choices=DAY_OF_THE_WEEK)
    from_hour = models.TimeField(null=True, blank=True)
    to_hour = models.TimeField(null=True, blank=True)

    def day_week_display_value(self):
        return dict(self.DAY_OF_THE_WEEK).get(self.day_week, '')

    def __unicode__(self):
        return "%s" % (self.day_week)

