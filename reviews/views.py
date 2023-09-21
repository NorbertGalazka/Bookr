from django.shortcuts import render, get_object_or_404

from .models import Book
from .utils import avarage_rating


def index(request):
    return render(request, "C:\\Users\\Norbert\\PycharmProjects\\Bookr\\reviews\\templates\\base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "C:\\Users\\Norbert\\PycharmProjects\\Bookr\\reviews\\templates\\search-results.html", {"search_text": search_text})


def book_list(request):
    books = Book.objects.all()
    books_with_reviews = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = avarage_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        books_with_reviews.append({"book": book, "book_rating": book_rating, "number_of_reviews": number_of_reviews})

    context = {
        "book_list": books_with_reviews
    }
    return render(request, "C:\\Users\\Norbert\\PycharmProjects\\Bookr\\reviews\\templates\\book_list.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = avarage_rating([review.rating for review in reviews])
        context = {
            "book": book,
            "book_rating": book_rating,
            "reviews": reviews
        }
    else:
        context = {
            "book": book,
            "book_rating": None,
            "reviews": None
        }
    return render(request, "C:\\Users\\Norbert\\PycharmProjects\\Bookr\\reviews\\templates\\book_detail.html", context)


