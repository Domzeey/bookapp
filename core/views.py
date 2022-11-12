from django.shortcuts import render, redirect
from .models import Author, book
from .forms import CreateBookForm
from django.contrib import messages

# Create your views here.


def home(request):
    books = book.objects.all()[1:4]
    if request.method == "POST":
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your book has been created")
            return redirect("home")
    else:
        form = CreateBookForm()
    context = {
        "books": books,
        "form": form
    }
    return render(request, "core/index.html", context)
