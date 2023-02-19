from rest_framework import serializers
from autores.models import Autor
from editoriales.models import Editorial
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id','nombre_completo','año_nacimiento','pais_origen','años_experiencia']

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ['id','nombre','año_fundacion']


class LibroSerializerResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField()
    año_publicacion = serializers.IntegerField()
    n_paginas = serializers.IntegerField()
    idioma = serializers.CharField()
    autor_id = serializers.IntegerField()
    editorial_id = serializers.IntegerField()
    autor = AutorSerializer(many=False,read_only=True)
    editorial = EditorialSerializer(many=False,read_only=True)


class LibroSerializersRequest(serializers.Serializer):
    titulo = serializers.CharField()
    año_publicacion = serializers.IntegerField()
    n_paginas = serializers.IntegerField()
    idioma = serializers.CharField()
