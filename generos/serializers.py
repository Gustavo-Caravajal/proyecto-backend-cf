from rest_framework import serializers

class GeneroSerializerResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    

class GeneroSerializerRequest(serializers.Serializer):
    nombre = serializers.CharField()
    