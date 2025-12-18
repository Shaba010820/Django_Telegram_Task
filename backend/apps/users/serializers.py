from rest_framework import serializers
from .models import User

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "telegram_id")