import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import DO_NOTHING


class Room(models.Model):
    room_code = str(uuid.uuid4())[:10]
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_code}"


class RoomDesignation(models.Model):
    room = models.ForeignKey(Room, related_name='designatedroom',
                             on_delete=models.DO_NOTHING)
    user = models.ForeignKey(
        User, related_name='roomusers', on_delete=DO_NOTHING)
