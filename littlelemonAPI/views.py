from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt;
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView


@api_view(['POST'])
def books(request):
    return Response('list of books' , status=status.HTTP_200_OK)


class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if author:
            return Response({"message: List of the books by the author : " + author}, status=status.HTTP_200_OK)  
        return Response({"message":"All books"}, status.HTTP_200_OK)
    def post(self, request):
       return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
    
class Book(APIView):
     def get(self, request , pk):
            return Response({"message":"Book is available with id : " + str(pk)}, status=status.HTTP_201_CREATED)

# Routing classes that extend viewsets
class BookView(viewsets.ViewSet):
    def list(self, request):
        return Response({"message":"All books"}, status.HTTP_200_OK)
    
    def create(self, request):
       return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        return Response({"message":"Updating a book"}, status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
        
    def partial_update(self, request, pk=None):
        return  Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
    def destroy(self, request, pk=None):
       return Response({"message":"Deleting a book"}, status.HTTP_200_OK)



# @csrf_exempt
# def books(request):
    # if request.method == "GET":
    # books = Book.objects.all().values()
    # return JsonResponse({"books": list(books)})
    # elif request.method == "POST":
    #     title = request.POST.get('title')
    #     author = request.POST.get('author')
    #     price = request.POST.get('price')

    #     book = Book(title= title, author= author, price= price)

    #     try:
    #         book.save()
    #     except IntegrityError:
    #         return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

    #     return JsonResponse(model_to_dict(books) , status=201)


# @csrf_exempt
# def book(request , pk):
#     if request.method == "GET":
#            book = Book.objects.get(pk=pk)
#            return JsonResponse({"book": book})
#     elif request.method == "PUT":
#          title = request.POST.get('title')
#          author = request.POST.get('author')
#          price = request.POST.get('price')

#          book = Book(title= title, author= author, price= price)

#          try:
#             book.save()
#          except IntegrityError:
#                 return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

#          return JsonResponse(model_to_dict(books) , status=201)
