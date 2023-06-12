from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('book-search', views.book_search),
    path('przywitanie',views.przywitanie)
]