from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),  # bookrent/
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


    #url(r'rentals/add/$', views.RentalCreate.as_view(), name='rental-add'),

    url(r'rentals/new/$', views.rental_new, name='rental-new'),
    url(r'rentals/(?P<pk>\d+)/edit/$', views.rental_edit, name='rental-edit'),





    #url(r'^articles/2003/$', views.special_case_2003),
   # url(r'^articles/([0-9]{4})/$', views.year_archive),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]