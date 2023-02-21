from rest_framework.response import Response
from rest_framework.decorators import api_view
from editoriales.models import Publisher
from editoriales.serializers import PublisherSerializerResponse
from editoriales.serializers import PublisherSerializerRequest
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET','POST'])
def publishers(request):

    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5 
        publishers = Publisher.objects.all()
        result_page = paginator.paginate_queryset(publishers, request)
        serializer = PublisherSerializerResponse(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    if request.method == 'POST':
        serializer = PublisherSerializerResponse(data=request.data)

        if serializer.is_valid():
            Publisher.objects.create(
                name = request.data['name'],
                founded_year = request.data['founded_year']
            )
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def detail_publishers(request,pk):
    publisher = Publisher.objects.get(pk=pk)

    if request.method == 'GET':
        ...

    if request.method == 'PUT':
        serializer = PublisherSerializerRequest(data=request.data)
        
        if serializer.is_valid():
            publisher.name = request.data['name']
            publisher.founded_year = request.data['founded_year']
            publisher.save()
    
    if request.method == 'DELETE':
        serializer = PublisherSerializerResponse(data=request.data)
        publisher.delete()
        return Response("DELETED PUBLISHER")

    serializer = PublisherSerializerResponse(publisher)
    
    return Response(serializer.data)