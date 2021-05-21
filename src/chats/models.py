from django.db import models
from rooms.models import Room


class Chat(models.Model):
    room = models.ForeignKey(Room, related_name='chatrooms',
                             on_delete=models.DO_NOTHING)
    msg = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
