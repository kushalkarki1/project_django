from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from home.models import Book
from home.forms import BookForm


def home_view(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "book_list.html", context)


def add_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("home:book_list"))
    return render(request, "form.html", {"form": form})


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("home:book_list"))
    return render(request, "form.html", {"form": form})