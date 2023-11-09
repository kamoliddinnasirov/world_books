from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book, BookInstance, Author
from django.views.generic import ListView, DetailView




def index(request):
    text_head = "Bizning saytimizda siz kitoblarni elektron ko'rinishda olishingiz mumkin!"
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact=2).count()
    authors = Author.objects
    num_authors = Author.objects.count()
    context = {"text_head" : text_head, 
               "books" : books, "num_books" : num_books,
               "num_instance" : num_instance,
               "num_instance_available" : num_instance_available,
               "authors" : authors, "num_authors" : num_authors
               }
    return render(request, 'index.html', context)


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = "books.html"
    paginate_by = 3

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "book_detail.html"


class AuthorListView(ListView):
    model = Author
    paginate_by = 3
    template_name = 'author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"



def about(request):
    text_head = "About company"
    name = "United International Company"
    rab1 = "Electronics books"
    rab2 = "Books scienes"
    rab3 = "Lorem ipsum1"
    rab4 = "Lorem ipsum2"
    context = {"text_head" : text_head, "name" : name,
               "rab1" : rab1, "rab2" : rab2,
               "rab3" : rab3, "rab4" : rab4,
               }
    
    return render(request, "about.html", context)


def contact(request):
    text_head = "Contact"
    name = "United International Company"
    address = "A.Navoiy 204"
    tel = "91-783-17-70"
    email = "kamoliddinnasirov@mail.ru"
    context = {
        "text_head" : text_head,
        "name" : name,
        "address" : address,
        "tel" : tel,
        "email" : email
    }

    return render(request, "contact.html", context)