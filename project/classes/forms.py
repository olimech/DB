from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ['name', 'author']
        fields = '__all__'


class AuthorBook(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'имя автора'}),
            'title': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'статус'})
        }

