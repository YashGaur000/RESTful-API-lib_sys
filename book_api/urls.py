#start
from django.contrib import admin
from book_api.views import BookList, BookCreate, BookDetail
from django.urls import path

urlpatterns = [
   # path('',Book.as_view()) ,
   path('',BookCreate.as_view()) ,
   path('list/',BookList.as_view()),
   path('<int:pk>',BookDetail.as_view())
]

# done
