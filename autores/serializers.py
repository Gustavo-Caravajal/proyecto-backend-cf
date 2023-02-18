from rest_framework import serializers


class AutorSerializerResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre_completo = serializers.CharField()
    año_nacimiento = serializers.IntegerField()
    pais_origen = serializers.CharField()
    años_experiencia = serializers.IntegerField()


class AutorSerializerRequest(serializers.Serializer):
    nombre_completo = serializers.CharField()
    año_nacimiento = serializers.IntegerField()
    pais_origen = serializers.CharField()
    años_experiencia = serializers.IntegerField()