from django.db import models
from ulid import ULID

def generate_ulid():
    return str(ULID())


class Category(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=26,
        default=generate_ulid,
        editable=False
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name