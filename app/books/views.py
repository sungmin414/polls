from django.shortcuts import render

# TemplateView
from django.views.generic import TemplateView, ListView, DetailView

from .models import Book, Author, Publisher


class BookModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super(BookModelView, self).get_context_data(**kwargs)
        context['object_list'] = ['Book', 'Author', 'Publisher']
        return context


# ListView
class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


# DetailView
class BookDetail(DetailView):
    model = Book


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher