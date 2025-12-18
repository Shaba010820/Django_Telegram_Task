from django.urls import path
from .views import TelegramAuthView

urlpatterns = [
    path("telegram/auth/", TelegramAuthView.as_view()),
]
