from django import forms
from .models import Books, ReviewBook


#class BooksForm(forms.Form):
#    title = forms.CharField(max_length=100, label="Title new book")
#    description = forms.CharField(widget=forms.Textarea, label="Description new book")
#    released_year = forms.IntegerField()


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'released_year']


class AuthorsForm(forms.Form):
    first_name = forms.CharField(max_length=20, label='Enter First name Author')
    last_name = forms.CharField(max_length=20, label='Enter Last name Author ')


class ReviewBookForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ReviewBook
        fields = ['rating', 'text']