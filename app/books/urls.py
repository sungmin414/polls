from django.urls import path

from . import views

app_name = 'books'

patterns = [
    path('', views.BooksModelView.as_view(), name='index'),
    path('books/', views.BookList.as_view(), name='book-list'),
    path('author/', views.AuthorList.as_view(), name='author-list'),
    path('publisher/', views.PublisherList.as_view(), name='publisher-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),
]