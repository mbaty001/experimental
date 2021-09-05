''' Define URL patterns for pizzerias  '''
from django.urls import path
from . import views

app_name = 'pizzeria'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pizzas page
    path('pizzas/', views.pizzas, name='pizzas'),
    # Get the particular pizza
    path('pizzas/<int:pizza_id>', views.pizza, name='pizza'),
]