from rest_framework import serializers

class PublisherSerializerResponse(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    founded_year = serializers.IntegerField()

class PublisherSerializerRequest(serializers.Serializer):
    name = serializers.CharField()
    founded_year = serializers.IntegerField()
