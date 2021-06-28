from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg

from .models import Book
# Create your views here.


def index(request):
    books_list = Book.objects.all().order_by("-rating")
    avg_rating = books_list.aggregate(Avg("rating"))
    total_books = books_list.count()

    return render(request, 'book_outlet/index.html', {
                  'books_list': books_list,
                  'avg_rating': avg_rating,
                  'total_books': total_books
                  })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestselling': book.is_bestselling
    })
