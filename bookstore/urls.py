from django.urls import path
from .views import books_list, books_info, books_django, authors_info, authors_list, author_books


urlpatterns = [
    path('', books_django, name='home'),
    path('books/', books_list, name='list'),
    path('authors/', authors_list, name='list_1'),
    path('books/<int:index_book>/', books_info, name='detail_books'),
    path('authors/<int:index_author>/', authors_info, name='detail_authors'),
    path('authors/<int:index_author>/author_books', author_books, name='author_books')
]
