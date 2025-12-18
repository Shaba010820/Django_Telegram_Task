from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "user",
        "category",
        "due_date",
        "created_at",
        "is_completed",
    )
    list_filter = ("is_completed", "category")
    search_fields = ("title",)