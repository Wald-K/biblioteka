from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    url(r'^$', views.index, name='home'),  # bookrent/
    url(r'books/$', views.BookListView.as_view(), name='book-list'),
    url(r'books/new/$', views.BookCreate.as_view(), name='book-new'),
    url(r'books/(?P<pk>\d+)/edit/$', views.BookUpdate.as_view(), name='book-edit'),
    url(r'books/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book-delete'),


    url(r'authors/$', views.AuthorListView.as_view(), name='author-list'),
    url(r'authors/new/$', views.AuthorCreate.as_view(), name='author-new'),
    url(r'authors/(?P<pk>\d+)/edit/$', views.AuthorUpdate.as_view(), name='author-edit'),
    url(r'authors/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author-delete'),



	url(r'clients/$', views.ClientListView.as_view(), name='client-list'),
    url(r'clients/new/$', views.ClientCreate.as_view(), name='client-new'),
    url(r'clients/(?P<pk>\d+)/edit/$', views.ClientUpdate.as_view(), name='client-edit'),
    url(r'clients/(?P<pk>\d+)/delete/$', views.ClientDelete.as_view(), name='client-delete'),
    url(r'clients/(?P<pk>\d+)/$', views.ClientDetail.as_view(), name='client-detail'),



    #url(r'rentals/add/$', views.RentalCreate.as_view(), name='rental-add'),
    # nowe wypozyczenie
    url(r'rentals/new/$', views.rental_new, name='rental-new'),
    # nowe wypozyczenie z widoku klienta gdy znamy jego id
    url(r'rentals/new/(?P<id_klienta>\d+)/$', views.rental_new_from_client_detail_template, name='rental-new_od_klienta'),
    # edycja wypozyczenia
    url(r'rentals/(?P<pk>\d+)/edit/$', views.rental_edit, name='rental-edit'),
    # zwrot z template klienta
    url(r'rentals/(?P<pk>\d+)/(?P<id_klienta>\d+)/zwrot_klient/$', views.rental_zwrot_klient, name='rental-zwrot-klient'), 
    # wszystkie wypozyczenia ktore juz zostaly zwrocone
    url(r'rentals/archival$', views.RentalArchivalListView.as_view(), name='rental-archival-list'),
    # wypozyczenia archiwalne danego klienta o numerze id_klienta
    url(r'rentals/archival/(?P<id_klienta>\d+)/$', views.rental_archival_list_by_client, name='rental-archival-list-by-klient'),






    #url(r'^articles/2003/$', views.special_case_2003),
   # url(r'^articles/([0-9]{4})/$', views.year_archive),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]