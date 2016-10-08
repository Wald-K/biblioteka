from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from models import Book, Author, Client, Rental
from django.urls import reverse_lazy

from . forms import RentalForm, RentalForm_without_Client
from django.shortcuts import redirect, get_object_or_404


# Create your views here.
@login_required(login_url='/accounts/login/') 
def index(request):
	contest = {'imie':request.user}
	return render(request, 'bookrent/home.html', contest)


# Book REST
class BookListView(ListView):
	model = Book
	def get_context_data(self, **kwargs):
		# context z generic view
		context = super(BookListView, self).get_context_data(**kwargs)
		# dodajemy swoj context  !!! jak dodac swoj wlasny contekst do generica
		# tutaj to jest bez sensu poniewaz zamiast imie wykorzystuje w base.html zmienna "user"
		context['imie'] = self.request.user
		return context
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(BookListView, self).dispatch(*args, **kwargs)

class BookCreate(CreateView):
	model = Book
	fields = '__all__'
	success_url = reverse_lazy('bookrent:book-list')

class BookUpdate(UpdateView):
	model = Book
	fields = '__all__'
	success_url = reverse_lazy('bookrent:book-list')

class BookDelete(DeleteView):
	model = Book
	success_url = reverse_lazy('bookrent:book-list')



# Author REST
class AuthorListView(ListView):
	model = Author

class AuthorCreate(CreateView):
	model = Author
	fields = '__all__'
	success_url = reverse_lazy('bookrent:author-list')

class AuthorUpdate(UpdateView):
	model = Author
	fields = '__all__'
	success_url = reverse_lazy('bookrent:author-list')
class AuthorDelete(DeleteView):
	model = Author
	success_url = reverse_lazy('bookrent:author-list')

	# Client REST
class ClientListView(ListView):
	model = Client

class ClientCreate(CreateView):
	model = Client
	fields = '__all__'
	success_url = reverse_lazy('bookrent:client-list')

class ClientUpdate(UpdateView):
	model = Client
	fields = '__all__'
	success_url = reverse_lazy('bookrent:client-list')
class ClientDelete(DeleteView):
	model = Client
	success_url = reverse_lazy('bookrent:client-list')

class ClientDetail(DetailView):
	model = Client

'''
class RentalCreate(CreateView):
	model = Rental
	fields = '__all__'
	success_url = reverse_lazy('bookrent:client-list')
'''

def rental_new(request):
	if request.method == "POST":
		form = RentalForm(request.POST)
		if form.is_valid():
			rental = form.save(commit=False)
			rental.save()
			return redirect('bookrent:client-list')
	else:
		form = RentalForm()
	return render(request, 'bookrent/rental_edit.html', {'form': form})


def rental_new_from_client_detail_template(request, id_klienta):
	if request.method == "POST":
		form = RentalForm_without_Client(request.POST)
		if form.is_valid():
			rental = form.save(commit=False)
			rental.client = Client.objects.get(pk=id_klienta)
			rental.save()
			return redirect('bookrent:client-detail', id_klienta)
	else:
		form = RentalForm_without_Client()
	return render(request, 'bookrent/rental_edit.html', {'form': form})




def rental_edit(request, pk):
	rental = get_object_or_404(Rental, pk=pk)
	if request.method == 'POST':
		form = RentalForm(request.POST, instance = rental)
		if form.is_valid():
			rental = form.save(commit=False)
			rental.save()
			return redirect('bookrent:client-list')
	else:
		form = RentalForm(instance = rental)
	return render(request, 'bookrent/rental_edit.html', {'form': form})

def rental_zwrot_klient(request, pk, id_klienta):
	rental = get_object_or_404(Rental, pk=pk)
	rental.returned = True
	rental.save()
	return redirect('bookrent:client-detail', id_klienta)