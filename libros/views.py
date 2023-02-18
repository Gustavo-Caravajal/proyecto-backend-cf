from rest_framework.response import Response
from rest_framework.decorators import api_view
from libros.models import Libro
from libros.serializers import LibroSerializerResponse
from libros.serializers import LibroSerializersRequest 
# Create your views here.

@api_view(['GET','POST'])
def libros(request):
    
    if request.method == 'GET':
        libros = Libro.objects.all()
        serializer = LibroSerializerResponse(libros,many=True)
        return Response(serializer.data)
    
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

