# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Pizza, Schedules

def index(request):
    pizza_list = Pizza.objects.order_by('code')
    schedules = Schedules.objects.order_by('day_week')
    context = {
            'pizza_list': pizza_list,
            'schedules': schedules
    }
    return render(request, 'portal/index.html', context)

