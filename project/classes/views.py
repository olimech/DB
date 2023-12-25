from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from .forms import BookForm, AuthorBook
from django.views import View
from django.views.generic import CreateView, UpdateView

# class BookCreateView(UpdateView):
#     model = Book
#     fields = ('name', 'author')
#     template_name = 'undex.html'
#     context_object_name = 'authors'
#     success_url = 'author'


class BookCreateView(CreateView):
    model = Book
    fields = ('name', 'author')
    template_name = 'undex.html'
    context_object_name = 'authors'
    success_url = 'author'

def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author')
    return render(request, 'classes/undex.html', context={'form': BookForm(), 'authors': Author.objects.all()})


def author(request):
    if request.method == 'POST':
        form = AuthorBook(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'classes/undex.html', context={'form': AuthorBook})


def updateBook(request, id):
    # book = Book.objects.get(id=id)
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = AuthorBook(request.POST, instance=BookForm)
        if form.is_valid():
            form.save()
    return render(request, 'classes/updatebook.html', context={'form': AuthorBook(instance=book)})


class BookView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'classes/undex.html', context={'form': BookForm(), 'authors': Book.objects.all()})

    def post(self, request, *args, **kwargs):
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('author')
            return self.get(request)





