from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
def show_books(request):

    all_books_obj = Book.objects.all()
    dict1  = {"books": all_books_obj}
    return render(request, template_name="home.html", context=dict1)


def add_book(request):

    if request.method == "POST":
        data = request.POST
        title = data["title"]
        author = data["author"]
        date = data["date"]
        isbn = data["isbn"]
        
        isbn_check_obj = Book.objects.filter(isbn = isbn)
        if isbn_check_obj:
            messages.info(request, "Isbn Id already present")    
            return render(request, template_name="add_book.html")
        book_obj = Book.objects.create(title = title, author = author, publication_date = date, isbn = isbn)
        messages.success(request, "Book inserted successfully")
        return render(request, template_name="add_book.html")
        
    return render(request, template_name="add_book.html")

def update_book(request):
    if request.method == "POST":
        data = request.POST
        isbn = data["isbn"]

        book_obj = Book.objects.filter(isbn = isbn)
        if not book_obj:
            messages.info(request, "Entry not Present")    
            return render(request, template_name="update.html")

        if data["title"]:
            title = data["title"]
        else:
            title = book_obj[0].title

        if data["author"]:
            author = data["author"]
        else:
            author = book_obj[0].author

        if data["date"]:
            date = data["date"]
        else:
            date = book_obj[0].publication_date

                
        book_obj = book_obj.update(title = title, author=author, publication_date = date) 
        messages.success(request, "Book successfully deleted")
        return redirect("/home/")
    
    return render(request, template_name="update.html")


def delete_book(request):
    if request.method == "POST":
        data = request.POST
        isbn = data["isbn"]
        
        isbn_check_obj = Book.objects.filter(isbn = isbn)
        if not isbn_check_obj:
            messages.info(request, "Isbn Id Not present: cannot be deleted")    
            return render(request, template_name="delete.html")
        
        isbn_check_obj.delete()
        messages.success(request, "Book successfully deleted")
        return redirect("/home/")
    
    return render(request, template_name="delete.html")
        

# Create your views here.
