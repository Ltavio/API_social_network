from django.db import models

import uuid


class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127, null=False, unique=True)
    email = models.EmailField(max_length=127, null=False, unique=True)
    phone = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="contacts",
    )
