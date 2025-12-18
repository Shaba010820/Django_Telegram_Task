from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "telegram_id", "is_staff")
    search_fields = ("username", "telegram_id")