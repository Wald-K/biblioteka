from django import forms

from . models import Rental
from django.core.exceptions import ValidationError





from django.core.exceptions import ValidationError


class RentalForm(forms.ModelForm):
	class Meta:
		model = Rental
		fields = '__all__'
	
	'''
	Zabezpieczenie by nie mozna bylo wypozyczyc ksiazki ktora juz jest wypozyczona
	'''	
	def clean(self):
		book_do_wyp = self.cleaned_data['book']
		rentals_this_book = Rental.objects.filter(book = book_do_wyp)

		for rental_this_book in rentals_this_book:
			if (rental_this_book.returned == False):
				raise ValidationError('Ksiazka juz wypozyczona.')


