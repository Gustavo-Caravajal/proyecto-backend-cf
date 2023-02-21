from rest_framework import serializers

class GenreSerializerResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    

class GenreSerializerRequest(serializers.Serializer):
    name = serializers.CharField()
    