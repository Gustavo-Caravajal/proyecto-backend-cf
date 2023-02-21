from rest_framework import serializers
from autores.models import Author
from editoriales.models import Publisher
from generos.models import Genre
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','full_name','birth_year','country_origin','years_experience']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id','name','founded_year']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']



class BookSerializerResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    publication_year = serializers.IntegerField()
    n_pages = serializers.IntegerField()
    languaje = serializers.CharField()
    author_id = serializers.IntegerField()
    publisher_id = serializers.IntegerField()
    author = AuthorSerializer(many=False,read_only=True)
    publisher = PublisherSerializer(many=False,read_only=True)

class BookSerializerResponsev4(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    publication_year = serializers.IntegerField()
    n_pages = serializers.IntegerField()
    languaje = serializers.CharField()
    author_id = serializers.IntegerField()
    publisher_id = serializers.IntegerField()
    genre_id = serializers.IntegerField()
    author = AuthorSerializer(many=False,read_only=True)
    publisher = PublisherSerializer(many=False,read_only=True)
    genre = GenreSerializer(many=False,read_only=True)

class BookSerializersRequest(serializers.Serializer):
    title = serializers.CharField()
    publication_year = serializers.IntegerField()
    n_pages = serializers.IntegerField()
    languaje = serializers.CharField()
