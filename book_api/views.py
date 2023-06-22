# use ctrl + / to comment all at once

# from django.shortcuts import render
# from book_api.models import Book
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from book_api.serializer import BookSerializer
# # Create your views here.

# @api_view(['GET'])
# def books_list(request):
#     books=Book.objects.all() #complex data
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def books_create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','DELETE'])
# def book_number(request,pk):
#     try:
#         book=Book.objects.get(pk=pk) 
#     except:
#         return Response({
#             'error':'Book does not found'
#         }, status=status.HTTP_404_NOT_FOUND)
#     if request.method=='GET':   
#         serializer=BookSerializer(book)
#         return Response(serializer.data)
    
#     if request.method=='PUT':
#         serializer=BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     if request.method=='DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#start with classes lets see

from rest_framework.views import APIView
from book_api.models import Book
from rest_framework.response import Response
from book_api.serializer import BookSerializer
from rest_framework import status

class BookList(APIView): #inheritance of apiview
    def get(self, request):
        books=Book.objects.all()
        serializer=BookSerializer(books, many=True)
        return Response(serializer.data)
    
    # def post(self, request):
    #     return Response({
    #         'best':'friend'
    #     })

class BookCreate(APIView):
    def post(self, request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({
                'error':'Book does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        book=self.get_book_by_pk(pk)
        serializer=BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book=self.get_book_by_pk(pk)
        serializer=BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book=self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
    # done
