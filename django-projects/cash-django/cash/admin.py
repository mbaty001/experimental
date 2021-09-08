from django.contrib import admin

from .models import Person, Entry

admin.site.register(Person)
admin.site.register(Entry)
