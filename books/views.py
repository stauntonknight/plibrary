from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from books.models import Book

class ListBookView(ListView):
    model = Book
    template_name = 'list_books.html'


class NewBookView(CreateView):
    model = Book
    template_name = 'edit_book.html'

    def get_success_url(self):
        return reverse('list-book')

class EditBookView(UpdateView):
    model = Book
    template_name = 'edit_book.html'
    def get_success_url(self):
        return reverse('list-book')
