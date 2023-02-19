from rest_framework.response import Response
from rest_framework.decorators import api_view
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializerResponse
from editoriales.serializers import EditorialSerializerRequest
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET','POST'])
def editoriales(request):

    if request.method == 'GET':
        paginador = PageNumberPagination()
        paginador.page_size = 5 
        editoriales = Editorial.objects.all()
        resultado_pagina = paginador.paginate_queryset(editoriales, request)
        serializer = EditorialSerializerResponse(resultado_pagina, many=True)
        return paginador.get_paginated_response(serializer.data)

    if request.method == 'POST':
        serializer = EditorialSerializerResponse(data=request.data)

        if serializer.is_valid():
            Editorial.objects.create(
                nombre = request.data['nombre'],
                año_fundacion = request.data['año_fundacion']
            )
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def detallar_editoriales(request,pk):
    editorial = Editorial.objects.get(pk=pk)

    if request.method == 'GET':
        ...

    if request.method == 'PUT':
        serializer = EditorialSerializerRequest(data=request.data)
        
        if serializer.is_valid():
            editorial.nombre = request.data['nombre']
            editorial.año_fundacion = request.data['año_fundacion']
            editorial.save()
    
    if request.method == 'DELETE':
        serializer = EditorialSerializerResponse(data=request.data)
        editorial.delete()
        return Response("EDITORIAL ELIMINADA")

    serializer = EditorialSerializerResponse(editorial)
    
    return Response(serializer.data)