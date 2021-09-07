from django import forms
from django.forms import widgets
from .models import Entry, Person
import datetime

YEAR_CHOICES = [(r,r) for r in range(2007, datetime.date.today().year+1)]
MONTH_CHOICES = [(m,m) for m in range(1,13)]

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        #year = forms.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
        #month = forms.DecimalField(('month'), choices=MONTH_CHOICES, default=datetime.datetime.now().month)
        #entry_date = forms.DateTimeField(('entry_date'), default=datetime.datetime.now())
        #person = forms.ModelMultipleChoicesField(queryset=Person.objects.all())
        fields = ['year', 'month', 'entry_date', 'person']