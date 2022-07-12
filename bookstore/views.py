from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy

from .models import Books, Authors, books, authors
from .forms import BooksForm, ReviewBookForm
from django.views.generic.base import View
from django.views.generic import TemplateView, FormView
from django.views.generic.detail import DetailView


# начальная страница с TemplateView вместо функции  books_django
class BaseView(TemplateView):
    template_name = 'books/bookstore.html'


# классом преобразуем наш books_list
class BooksView(View):

    def post(self, request):
        form = BooksForm(request.POST)
        books = Books.objects.all()
        if form.is_valid():
            form.save()
        context = {'books': books, 'book_form': BooksForm}
        return render(request, 'books/books_list.html', context=context)

    def get(self, request):
        books = Books.objects.all().order_by('title')
        search = ''
        if request.method == 'GET' and 'search' in request.GET:
            search = request.GET['search']
            books = books.filter(title__icontains=search)
        context = {'books': books, 'search': search, 'book_form': BooksForm}
        return render(request, 'books/books_list.html', context=context)


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

    context = {'books': books, 'books': books.order_by('title'), 'search': search, 'book_form': BooksForm}
    return render(request, 'books/books_list.html', context=context)


class BooksDetail(DetailView):
    model = Books
    template_name = 'books/books_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['book_review_form'] = ReviewBookForm()
        return context


# вьюха для  рецензій
class ReviewDetail(FormView):
    form_class = ReviewBookForm
    success_url = reverse_lazy('detail_books')
    template_name = 'books/books_info.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = Books.objects.get(id=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self, *args):
        return reverse_lazy('detail_books', kwargs=self.kwargs)


# список авторов и сортировка по id
class AuthorsView(View):
    def get(self, request):
        authors = Authors.objects.all().order_by('last_name')
        qwerty = ''
        if request.method == 'GET' and 'qwerty' in request.GET:
            qwerty = request.GET['qwerty']
            authors = authors.filter(id=qwerty)
        context = {'authors': authors, 'qwerty': qwerty}
        return render(request, 'authors/authors_list.html', context=context)


def authors_list(request):
    authors = Authors.objects.all()
    qwerty = ''
    if request.method == 'GET' and 'qwerty' in request.GET:
        qwerty = request.GET['qwerty']
        authors = authors.filter(id=qwerty)
    context = {'authors': authors.order_by('last_name'), 'qwerty': qwerty}
    return render(request, 'authors/authors_list.html', context=context)


# информация про автора по книге
class AuthorsDetail(DetailView):
    model = Authors
    template_name = 'authors/authors_info.html'


def authors_info(request, index_author):
    author = get_object_or_404(Authors, pk=index_author)
    context = {'author': author}
    return render(request, 'authors/authors_info.html', context=context)


# спикок книг по автору
class AuthorBooks:
    pass


def author_books(request, index_author):
    author_books = list(filter(lambda book: book['author_id'] == index_author, books))
    context = {'author_books': author_books}
    return render(request, 'authors/author_books.html', context=context)


# Добавить новую книгу
class CreateBookView(View):
    def post(self, request):
        books = Books.objects.all()
        if request.method == 'POST':
            form = BooksForm(request.POST)
            if form.is_valid():
                form.save()
                books = Books.objects.all()
            context = {'books': books, 'book_form': BooksForm}
            return render(request, 'books/add_book.html', context=context)


def add_book(request):
    books = Books.objects.all()
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            books = Books.objects.all()
            # from class Form
            # data = form.cleaned_data
            # title = data['title']
            # description = data['description']
            # released_year = data['released_year']
            # Books.objects.create(title=title, description=description, released_year=released_year)
            # books = Books.objects.all()
    context = {'books': books, 'book_form': BooksForm}
    return render(request, 'books/add_book.html', context=context)
