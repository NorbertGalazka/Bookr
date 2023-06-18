from django.shortcuts import render, get_object_or_404

from .models import Book
from .utils import avarage_rating


def book_list(request):
    books = Book.objects.all()
    books_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            avarege_rating = avarage_rating([review.rating for review in reviews])
            num_of_reviews = len(reviews)
        else:
            avarege_rating = None
            num_of_reviews = 0

        dict = {'book_object': book, 'avarege_rating': avarege_rating, 'num_of_reviews': num_of_reviews}
        books_list.append(dict)

    dict_to_html = {'books': books_list}

    return render(request, 'C:\\Users\\Norbert\\PycharmProjects\\Bookr\\reviews\\templates\\book_list.html', dict_to_html)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = avarage_rating([review.rating for review in reviews])
        context = {"book": book, "book_rating": book_rating, "reviews":reviews}

    else:
        context ={"book": book, "book_rating": None, "reviews":None}

    return render(request, "C:\\Users\\Norbert\\PycharmProjects\\Bookr\\reviews\\templates\\book_detail.html", context)



