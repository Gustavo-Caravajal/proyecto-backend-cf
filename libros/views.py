from rest_framework.response import Response
from rest_framework.decorators import api_view
from libros.models import Libro
from libros.models import Libro_v4
from libros.serializers import LibroSerializerResponse
from libros.serializers import LibroSerializersRequest 
from libros.serializers import LibroSerializerResponse_v4
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET','POST'])
def libros(request):
    
    if request.method == 'GET':
        paginador = PageNumberPagination()
        paginador.page_size = 5
        libros = Libro.objects.all()
        resultado_pagina = paginador.paginate_queryset(libros,request)
        serializer = LibroSerializerResponse(resultado_pagina,many=True)
        return paginador.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = LibroSerializerResponse(data=request.data)

        if serializer.is_valid():
            Libro.objects.create(
                titulo = request.data['titulo'],
                año_publicacion = request.data['año_publicacion'],
                n_paginas = request.data['n_paginas'],
                idioma = request.data['idioma'],
                autor_id = request.data['autor_id'],
                editorial_id = request.data['editorial_id']     
            )
            return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def detallar_libros(request,pk):
    libro = Libro.objects.get(pk=pk)
    if request.method == 'GET':
        ...

    if request.method == 'PUT':
        serializer = LibroSerializersRequest(data=request.data)
        if serializer.is_valid():
            libro.titulo = request.data['titulo']
            libro.año_publicacion = request.data['año_publicacion']
            libro.n_paginas = request.data['n_paginas']
            libro.idioma = request.data['idioma']
            libro.save()
    
    if request.method == 'DELETE':
        serializer = LibroSerializerResponse(data=request.data)
        libro.delete()
        return Response("LIBRO ELIMINADO")
    
    serializer = LibroSerializerResponse(libro)

    return Response(serializer.data)   



#libro api version 4

@api_view(['GET','POST'])
def libros_v4(request):
    
    if request.method == 'GET':
        paginador = PageNumberPagination()
        paginador.page_size = 5
        libros = Libro_v4.objects.all()
        resultado_pagina = paginador.paginate_queryset(libros,request)
        serializer = LibroSerializerResponse_v4(resultado_pagina,many=True)
        return paginador.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = LibroSerializerResponse_v4(data=request.data)

        if serializer.is_valid():
            Libro_v4.objects.create(
                titulo = request.data['titulo'],
                año_publicacion = request.data['año_publicacion'],
                n_paginas = request.data['n_paginas'],
                idioma = request.data['idioma'],
                autor_id = request.data['autor_id'],
                editorial_id = request.data['editorial_id'],
                genero_id = request.data['genero_id']    
            )
            return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def detallar_libros_v4(request,pk):
    libro = Libro_v4.objects.get(pk=pk)
    if request.method == 'GET':
        ...

    if request.method == 'PUT':
        serializer = LibroSerializersRequest(data=request.data)
        if serializer.is_valid():
            libro.titulo = request.data['titulo']
            libro.año_publicacion = request.data['año_publicacion']
            libro.n_paginas = request.data['n_paginas']
            libro.idioma = request.data['idioma']
            libro.save()
    
    if request.method == 'DELETE':
        serializer = LibroSerializerResponse_v4(data=request.data)
        libro.delete()
        return Response("LIBRO ELIMINADO")
    
    serializer = LibroSerializerResponse_v4(libro)

    return Response(serializer.data)   
