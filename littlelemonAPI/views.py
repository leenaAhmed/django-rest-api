from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt;
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from .models import MenuItem, Book , Category
from .serializers import MenuItemSerializer , CategorySerializer
from django.shortcuts import get_object_or_404

class MenuItemView(generics.ListCreateAPIView):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView , generics.DestroyAPIView):
      queryset = MenuItem.objects.all()
      serializer_class = MenuItemSerializer


@api_view(['GET', 'POST'])
def menu_items(request):
    # items = MenuItem.objects.all()
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        serialized_item = MenuItemSerializer(items, many=True, context={'request': request})
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(items=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)


@api_view()
def menu_item(request, menuId):
    items = get_object_or_404(MenuItem, pk=menuId)
    serializer_items = MenuItemSerializer(items)
    return Response(serializer_items.data, status=status.HTTP_200_OK)

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer_category = CategorySerializer(category)
    return Response(serializer_category.data, status=status.HTTP_200_OK)

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



@csrf_exempt
def booksList(request):
    if request.method == "GET":
        books = Book.objects.all().values()
        return JsonResponse({"books": list(books)})
    elif request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        book = Book(title= title, author= author, price= price)

        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

        return JsonResponse(model_to_dict(books) , status=201)


@csrf_exempt
def single_book(request , pk):
    if request.method == "GET":
           book = Book.objects.get(pk=pk)
           return JsonResponse({"book": book})
    elif request.method == "PUT":
         title = request.POST.get('title')
         author = request.POST.get('author')
         price = request.POST.get('price')

         book = Book(title= title, author= author, price= price)

         try:
            book.save()
         except IntegrityError:
                return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

         return JsonResponse(model_to_dict(book) , status=201)
