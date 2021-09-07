import django
from django.db import models
import datetime

YEAR_CHOICES = [(r,r) for r in range(2007, datetime.date.today().year+1)]
MONTH_CHOICES = [(m,m) for m in range(1,13)]

class Person(models.Model):
	name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=20)

	def __str__(self):
		return (f'{self.name} {self.last_name}')

class Entry(models.Model):
	year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)	
	month = models.DecimalField(max_digits=2, decimal_places=0, choices=MONTH_CHOICES, default=datetime.datetime.now().month)
	entry_date = models.DateTimeField(default=django.utils.timezone.now)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)

	def __str__(self):
		return (f'{self.person.name}: {self.year}-{self.month} {self.entry_date}')

	class Meta():
		verbose_name_plural = 'Entries'