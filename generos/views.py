from rest_framework.response import Response
from rest_framework.decorators import api_view
from generos.models import Genero
from generos.serializers import GeneroSerializerResponse
from generos.serializers import GeneroSerializerRequest
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET','POST'])
def generos(request):
    if request.method == 'GET':
        paginador = PageNumberPagination()
        paginador.page_size = 5
        generos = Genero.objects.all()
        resultado_pagina = paginador.paginate_queryset(generos,request)
        serializer = GeneroSerializerResponse(resultado_pagina,many=True)
        return paginador.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = GeneroSerializerResponse(data=request.data)

        if serializer.is_valid():
            Genero.objects.create(
                nombre = request.data['nombre']
            )
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def detallar_generos(request,pk):
    genero = Genero.objects.get(pk=pk)

    if request.method == 'GET':
        ...

    if request.method == 'PUT':
        serializer = GeneroSerializerRequest(data=request.data)

        if serializer.is_valid():
            genero.nombre = request.data['nombre']
            genero.save()
    
    if request.method == 'DELETE':
        serializer = GeneroSerializerResponse(data=request.data)
        genero.delete()
        return Response('GENERO ELIMINADO')

    return Response(serializer.data)