
from django.contrib import admin
from book_api.views import books_list, books_create, book_number
from django.urls import path

urlpatterns = [
   path('',books_create) ,
   path('list/',books_list),
   path('<int:pk>',book_number)
]
