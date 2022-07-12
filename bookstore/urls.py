from django.urls import path
from .views import BaseView, BooksView, BooksDetail, AuthorsView, AuthorsDetail, author_books, add_book, ReviewDetail


urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('books/', BooksView.as_view(), name='list'),
    path('authors/', AuthorsView.as_view(), name='list_1'),
    path('books/<int:pk>/', BooksDetail.as_view(), name='detail_books'),
    path('books/<int:pk>/reviews/', ReviewDetail.as_view(), name='reviews_book'),
    path('authors/<int:pk>/', AuthorsDetail.as_view(), name='detail_authors'),
    path('authors/<int:index_author>/author_books', author_books, name='author_books'),
    path('add_book/', add_book, name='add_book'),
]
