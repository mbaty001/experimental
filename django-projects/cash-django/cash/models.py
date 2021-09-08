from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=20)

	def __str__(self):
		return ('%s %s' %(self.name, self.last_name))


class Entry(models.Model):
	year = models.DecimalField(max_digits=4, decimal_places=0)
	month = models.DecimalField(max_digits=2, decimal_places=0)
	entry_date = models.DateTimeField()
	person = models.ForeignKey(Person, on_delete=models.CASCADE)

	def __str__(self):
		return ('%s: %s-%s' %(self.person.name, self.year, self.month))

	class Meta():
                verbose_name_plural = 'Entries'

