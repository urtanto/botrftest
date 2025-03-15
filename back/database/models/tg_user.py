import uuid
from tortoise import models
from tortoise.fields import UUIDField, TextField, DateField


class TgUser(models.Model):
    id = UUIDField(pk=True, default=uuid.uuid4)
    tg_id = TextField(unique=True)
    first_name = TextField(null=True)
    last_name = TextField(null=True)
    username = TextField()
    birth_date = DateField()

    class Meta:
        table = "tg_user"