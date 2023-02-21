from rest_framework.response import Response
from rest_framework.decorators import api_view
from authors.models import Author
from authors.serializers import AuthorSerializerResponse
from authors.serializers import AuthorSerializerRequest
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET','POST'])
def authors(request):

    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5
        authors = Author.objects.all()
        resultado_pagina = paginator.paginate_queryset(authors,request)
        serializer = AuthorSerializerResponse(resultado_pagina,many=True)
        return paginator.get_paginated_response(serializer.data)

    if request.method == 'POST':
        serializer = AuthorSerializerResponse(data=request.data)

        if serializer.is_valid():
            Author.objects.create(
                full_name = request.data['full_name'],
                birth_year = request.data['birth_year'],
                country_origin  = request.data['country_origin'],
                years_experience = request.data['years_experience']
            )
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def detail_authors(request,pk):
    author = Author.objects.get(pk=pk)
    if request.method == 'GET':
        ...

    if request.method == 'PUT':
        serializer = AuthorSerializerRequest(data=request.data)
        if serializer.is_valid():
            author.full_name = request.data['full_name']
            author.birth_year = request.data['birth_year']
            author.country_origin = request.data['country_origin']
            author.years_experience = request.data['years_experience']
            author.save()
    
    if request.method == 'DELETE':
        serializer = AuthorSerializerResponse(data=request.data)
        author.delete()
        return Response("DELETED AUTHOR")

    serializer = AuthorSerializerResponse(author)
    
    return Response(serializer.data)
