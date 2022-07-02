from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound

from .models import Books, Authors, books, authors
from .forms import BooksForm


# начальная страница
def books_django(request):
    return render(request, 'books/bookstore.html')


# список книг, определиться какой вид форм будет html or class_forms
def books_list(request):
    books = Books.objects.all()
    search = ''
    if request.method == 'GET' and 'search' in request.GET:
        search = request.GET['search']
        books = books.filter(title__icontains=search)
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            books = Books.objects.all()

    context = {'books':books, 'books': books.order_by('title'), 'search': search, 'book_form': BooksForm}
    return render(request, 'books/books_list.html', context=context)


# информация по книге, проброска ошибки на несущ страницу Http404 or get_object_or_404
def books_info(request, index_book):
    book = get_object_or_404(Books, pk=index_book)
    context = {'book': book}
    return render(request, 'books/books_info.html', context=context)


# список авторов и сортировка по id
def authors_list(request):
    authors = Authors.objects.all()
    qwerty = ''
    if request.method == 'GET' and 'qwerty' in request.GET:
        qwerty = request.GET['qwerty']
        authors = authors.filter(id=qwerty)
    context = {'authors': authors.order_by('last_name'), 'qwerty': qwerty}
    return render(request, 'authors/authors_list.html', context=context)


# информация про автора по книге
def authors_info(request, index_author):
    author = get_object_or_404(Authors, pk=index_author)
    context = {'author': author}
    return render(request, 'authors/authors_info.html', context=context)


# спикок книг по автору
def author_books(request, index_author):
    author_books = list(filter(lambda book: book['author_id'] == index_author, books))
    context = {'author_books': author_books}
    return render(request, 'authors/author_books.html', context=context)


# Добавить новую книгу
def add_book(request):
    books = Books.objects.all()
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            books = Books.objects.all()
            # from class Form
            #data = form.cleaned_data
            #title = data['title']
            #description = data['description']
            #released_year = data['released_year']
            #Books.objects.create(title=title, description=description, released_year=released_year)
            #books = Books.objects.all()
    context = {'books': books, 'book_form': BooksForm}
    return render(request, 'books/add_book.html', context=context)
