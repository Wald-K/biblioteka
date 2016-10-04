from django import forms

from . models import Rental
from django.core.exceptions import ValidationError





from django.core.exceptions import ValidationError

def validate_czy_ksiazka_dostepna(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

class RentalForm(forms.ModelForm):
	class Meta:
		model = Rental
		fields = '__all__'
	'''def clean_book(self):
		data = self.cleaned_data['book']
		if data.title == "Wanda":
			raise forms.ValidationError("Wanda")
		return data'''
	def clean(self):
		book_do_wyp = self.cleaned_data['book']
		rentals_this_book = Rental.objects.filter(book = book_do_wyp)

		for rental_this_book in rentals_this_book:
			if (rental_this_book.returned == False):
				raise ValidationError('Ksiazka wypozyczona.')


