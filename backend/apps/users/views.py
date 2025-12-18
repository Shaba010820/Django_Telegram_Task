from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import TelegramUserSerializer


@method_decorator(csrf_exempt, name="dispatch")
class TelegramAuthView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    parser_classes = [JSONParser]

    def post(self, request):
        telegram_id = request.data.get("telegram_id")
        username = request.data.get("username")

        if telegram_id is None:
            return Response(
                {"error": "telegram_id is required"},
                status=400,
            )

        user, _ = User.objects.get_or_create(
            telegram_id=telegram_id,
            defaults={"username": username or f"tg_{telegram_id}"}
        )

        serializer = TelegramUserSerializer(user)
        return Response(serializer.data)