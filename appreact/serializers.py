from rest_framework import serializers
from .models import Todo, EurUsd

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id' ,'title', 'description', 'completed')


class EurUsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = EurUsd
        fields = ('id' , 'timestamp', 'open', 'close', 'high', 'low', 'volume', 'date', 'month', 'day', 'hour', 'minute', 'direction')
