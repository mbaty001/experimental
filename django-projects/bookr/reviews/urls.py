from django.urls import path, include
from . import views 

app_name = 'reviews'

urlpatterns = [
    path('book-search/', views.search, name='search'),
    path('', views.welcome_view, name='welcome_view')
]