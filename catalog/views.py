from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from catalog.models import Book, BookInstance, Author
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import Add_authors, Form_edit_author, BookModelForm
from django.urls   import reverse
from django.urls import reverse_lazy




class BookCreate(CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy("edit_books")
    template_name = "book_form.html"


class BookUpdate(UpdateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy("edit_books")

class BookDelete(DeleteView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy("edit_books")
    template_name = "book_confirm_delete.html"




def edit_books(request):
    book = Book.objects.all()
    context = {"book" : book}
    return render(request, "edit_books.html", context)



def edit_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        instance = Author.objects.get(pk=id)
        form = Form_edit_author(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/edit_authors/")
        
        else:
            form = Form_edit_author(instance=author)
            content = {"form":form}
            return render(request, "edit_author.html", content)





def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/edit_authors/")
    except:
        return HttpResponseNotFound("<h2>Author not found!</h2>")



def add_author(request):
    if request.method == "POST":
        form = Add_authors(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            date_of_birth = form.cleaned_data.get("date_of_birth")
            about = form.cleaned_data.get("about")
            photo = form.cleaned_data.get("photo")
            # create data
            obj = Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                about=about,
                photo=photo
                )
            # save data
            obj.save()
            # refresh in list data author
            return HttpResponseRedirect(reverse("author-list"))
    else:
        form = Add_authors()
        context = {"form" : form}
        return render(request, "author_add.html", context)
        




class LoadetBooksByUser(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'bookinstance_list_customer.html'
    paginate_by = 10
    def get_queryset(self) -> QuerySet[Any]:
        return BookInstance.objects.filter(customer=self.request.user).filter(status__exact='2').order_by("due_back")
    


def edit_authors(request):
    author = Author.objects.all()
    context = {"author" : author}
    return render(request, "edit_authors.html", context)



def index(request):
    text_head = "Bizning saytimizda siz kitoblarni elektron ko'rinishda olishingiz mumkin!"
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact=2).count()
    authors = Author.objects
    num_authors = Author.objects.count()

    # visited
    num_visits = request.session.get("num_visits", 0)
    request.session['num_visits'] = num_visits + 1



    context = {"text_head" : text_head, 
               "books" : books, "num_books" : num_books,
               "num_instance" : num_instance,
               "num_instance_available" : num_instance_available,
               "authors" : authors, "num_authors" : num_authors,
               "num_visits" : num_visits
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