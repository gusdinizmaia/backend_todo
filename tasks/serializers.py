from django.db import serializers


# Create your serializers here.
class STATUS_CHOICES(serializers.TextChoices):
    CONCLUDE = "conclude"
    PENDANT = "pendant"


class Task(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    date = serializers.DateTime()
    duration = serializers.TimeField()
    status = serializers.CharField(
        choices=STATUS_CHOICES, default=STATUS_CHOICES.PENDANT
    )

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        if validated_data.get("password"):
            instance.set_password(validated_data["password"])
            instance.save()

        return instance
