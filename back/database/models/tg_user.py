import uuid
from tortoise import models
from tortoise.fields import UUIDField, TextField, CharField, DatetimeField


class TgUser(models.Model):
    id = UUIDField(pk=True, default=uuid.uuid4)
    tg_id = CharField(max_length=30, unique=True)
    first_name = TextField(null=True)
    last_name = TextField(null=True)
    username = TextField()
    birth_date = DatetimeField()

    class Meta:
        table = "tg_user"