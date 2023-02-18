from rest_framework.response import Response
from rest_framework.decorators import api_view
from autores.models import Autor
from autores.serializers import AutorSerializerResponse
from autores.serializers import AutorSerializerRequest

# Create your views here.

@api_view(['GET','POST'])
def autores(request):

    if request.method == 'GET':
        autores = Autor.objects.all()
        serializer = AutorSerializerResponse(autores,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AutorSerializerResponse(data=request.data)

        if serializer.is_valid():
            Autor.objects.create(
                nombre_completo = request.data['nombre_completo'],
                año_nacimiento = request.data['año_nacimiento'],
                pais_origen = request.data['pais_origen'],
                años_experiencia = request.data['años_experiencia']
            )
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def detallar_autores(request,pk):
    autor = Autor.objects.get(pk=pk)
    if request.method == 'GET':
        ...

    if request.method == 'PUT':
        serializer = AutorSerializerRequest(data=request.data)
        if serializer.is_valid():
            autor.nombre_completo = request.data['nombre_completo']
            autor.año_nacimiento = request.data['año_nacimiento']
            autor.pais_origen = request.data['pais_origen']
            autor.años_experiencia = request.data['años_experiencia']
            autor.save()
    
    if request.method == 'DELETE':
        serializer = AutorSerializerResponse(data=request.data)
        autor.delete()
        return Response("AUTOR ELIMINADO")

    serializer = AutorSerializerResponse(autor)
    
    return Response(serializer.data)
