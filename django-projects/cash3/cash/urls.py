from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cash'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Stats page
    path('stats/', views.stats, name='stats'),
    # Add new entry
    path('new_entry/', views.new_entry, name='new_entry'),
    # Edit entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]