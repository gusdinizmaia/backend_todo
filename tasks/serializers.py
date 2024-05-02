from rest_framework import serializers
from .models import Task


# Create your serializers here.
class STATUS_CHOICES:
    CONCLUDE = "conclude"
    PENDANT = "pendant"


class TaskSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    date = serializers.DateField()
    duration = serializers.TimeField()
    status = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        return instance

    class Meta:
        model = Task
        fields = ["id", "title", "description", "date", "duration", "status"]
