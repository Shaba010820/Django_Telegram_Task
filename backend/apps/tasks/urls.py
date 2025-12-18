from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TelegramTaskView

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")


urlpatterns = [
    path("telegram/tasks/", TelegramTaskView.as_view()),
]

urlpatterns += router.urls