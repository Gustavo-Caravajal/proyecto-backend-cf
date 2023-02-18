from rest_framework import serializers

class EditorialSerializerResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField()
    año_fundacion = serializers.IntegerField()

class EditorialSerializerRequest(serializers.Serializer):
    nombre = serializers.CharField()
    año_fundacion = serializers.IntegerField()
