from rest_framework.response import Response
from rest_framework.decorators import api_view
from libros.models import Book
from libros.models import BookV4
from libros.serializers import BookSerializerResponse
from libros.serializers import BookSerializersRequest 
from libros.serializers import BookSerializerResponsev4
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET','POST'])
def books(request):
    
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5
        books = Book.objects.all()
        result_page = paginator.paginate_queryset(books,request)
        serializer = BookSerializerResponse(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = BookSerializerResponse(data=request.data)

        if serializer.is_valid():
            Book.objects.create(
                title = request.data['title'],
                publication_year = request.data['publication_year'],
                n_pages = request.data['n_pages'],
                languaje = request.data['languaje'],
                author_id = request.data['author_id'],
                publisher_id = request.data['publisher_id']     
            )
            return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def detail_books(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        ...

    if request.method == 'PUT':
        serializer = BookSerializersRequest(data=request.data)
        if serializer.is_valid():
            book.title = request.data['title']
            book.publication_year = request.data['publication_year']
            book.n_pages = request.data['n_pages']
            book.languaje = request.data['languaje']
            book.save()
    
    if request.method == 'DELETE':
        serializer = BookSerializerResponse(data=request.data)
        book.delete()
        return Response("DELETED BOOK")
    
    serializer = BookSerializerResponse(book)

    return Response(serializer.data)   



#libro api version 4

@api_view(['GET','POST'])
def books_v4(request):
    
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5
        books = BookV4.objects.all()
        result_page = paginator.paginate_queryset(books,request)
        serializer = BookSerializerResponsev4(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = BookSerializerResponsev4(data=request.data)

        if serializer.is_valid():
            BookV4.objects.create(
                title = request.data['title'],
                publication_year = request.data['publication_year'],
                n_pages = request.data['n_pages'],
                languaje = request.data['languaje'],
                author_id = request.data['author_id'],
                publisher_id = request.data['publisher_id'],
                genre_id = request.data['genre_id']    
            )
            return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def detail_books_v4(request,pk):
    book = BookV4.objects.get(pk=pk)
    if request.method == 'GET':
        ...

    if request.method == 'PUT':
        serializer = BookSerializersRequest(data=request.data)
        if serializer.is_valid():
            book.title = request.data['title']
            book.publication_year = request.data['publication_year']
            book.n_pages = request.data['n_pages']
            book.languaje = request.data['languaje']
            book.save()
    
    if request.method == 'DELETE':
        serializer = BookSerializerResponsev4(data=request.data)
        book.delete()
        return Response("LIBRO ELIMINADO")
    
    serializer = BookSerializerResponsev4(book)

    return Response(serializer.data)   
