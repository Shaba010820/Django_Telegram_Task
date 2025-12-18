from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "category",
            "due_date",
            "created_at",
            "is_completed",
        )
        read_only_fields = ("id", "created_at")

class TelegramTaskCreateSerializer(serializers.ModelSerializer):
    telegram_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = (
            "telegram_id",
            "title",
            "description",
            "category",
            "due_date",
        )


class TelegramTaskSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", default=None)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "category",
            "created_at",
        )