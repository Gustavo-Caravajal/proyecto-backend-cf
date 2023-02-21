from rest_framework.response import Response
from rest_framework.decorators import api_view
from generos.models import Genre
from generos.serializers import GenreSerializerResponse
from generos.serializers import GenreSerializerRequest
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET','POST'])
def genres(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5
        genres = Genre.objects.all()
        result_page = paginator.paginate_queryset(genres,request)
        serializer = GenreSerializerResponse(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = GenreSerializerResponse(data=request.data)

        if serializer.is_valid():
            Genre.objects.create(
                name = request.data['name']
            )
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def detail_genres(request,pk):
    genre = Genre.objects.get(pk=pk)

    if request.method == 'GET':
        ...

    if request.method == 'PUT':
        serializer = GenreSerializerRequest(data=request.data)

        if serializer.is_valid():
            genre.name = request.data['name']
            genre.save()
    
    if request.method == 'DELETE':
        serializer = GenreSerializerResponse(data=request.data)
        genre.delete()
        return Response('DELETED GENRE')

    return Response(serializer.data)