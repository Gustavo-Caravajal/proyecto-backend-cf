from rest_framework import serializers


class AuthorSerializerResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name  = serializers.CharField()
    birth_year = serializers.IntegerField()
    country_origin  = serializers.CharField()
    years_experience = serializers.IntegerField()


class AuthorSerializerRequest(serializers.Serializer):
    full_name  = serializers.CharField()
    birth_year = serializers.IntegerField()
    country_origin  = serializers.CharField()
    years_experience = serializers.IntegerField()