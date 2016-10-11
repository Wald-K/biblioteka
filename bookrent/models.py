from __future__ import unicode_literals

from django.db import models
import datetime



# Create your models here.


class Author(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)

	def __unicode__(self):
		return '{0} {1}'.format(self.last_name, self.first_name)
	
	class Meta:
		ordering = ('last_name',)
		

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)

	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ('title',)


class Client(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	pesel = models.IntegerField(unique=True)
	address = models.TextField()
	def __unicode__(self):
		return '{0} {1}'.format(self.last_name, self.first_name)

	class Meta:
		ordering = ('last_name',)

	def number_of_not_returned_book(self):
		not_returned_book = 0
		for rental in self.rental_set.all():
			if rental.returned == False:
				not_returned_book = not_returned_book +1
		return not_returned_book




class Rental(models.Model):
	client = models.ForeignKey(Client)
	book = models.ForeignKey(Book)
	rental_date = models.DateField(default=datetime.date.today)
	returned = models.BooleanField(default=False)
	def __unicode__(self):
		return 'Rental: {0} | Klient: {1} | Ksiazka: {2}'.format(self.pk,self.client.last_name, self.book.title)

	
