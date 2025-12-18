from rest_framework import viewsets, status
from .serializers import TaskSerializer, TelegramTaskCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Task
from .serializers import TelegramTaskSerializer
from ..users.models import User


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



@method_decorator(csrf_exempt, name="dispatch")
class TelegramTaskView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_user(self, telegram_id: int) -> User | None:
        try:
            return User.objects.get(telegram_id=telegram_id)
        except User.DoesNotExist:
            return None

    def get(self, request):
        telegram_id = request.query_params.get("telegram_id")

        if not telegram_id:
            return Response(
                {"error": "telegram_id is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = self.get_user(int(telegram_id))
        if not user:
            return Response([], status=status.HTTP_200_OK)

        tasks = (
            Task.objects
            .filter(user=user)
            .select_related("category")
            .order_by("-created_at")
        )

        serializer = TelegramTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TelegramTaskCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        telegram_id = serializer.validated_data.pop("telegram_id")
        user = self.get_user(telegram_id)

        if not user:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        task = serializer.save(user=user)

        return Response(
            {"id": task.id},
            status=status.HTTP_201_CREATED,
        )
