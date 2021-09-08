from django.shortcuts import render
from .models import Pizza

def index(request):
    return render(request, 'pizzeria/index.html')

def pizzas(request):
    ''' Retrieve all pizzas '''
    pizzas = Pizza.objects.all()

    context = {'pizzas': pizzas}

    return render(request, 'pizzeria/pizzas.html', context)

def pizza(request, pizza_id):
    ''' Retrieve data for particular pizza'''
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()

    context = {'pizza': pizza, 'toppings': toppings}

    return render(request, 'pizzeria/pizza.html', context)

