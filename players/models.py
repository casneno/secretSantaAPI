from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Player(models.Model):
    display_name = models.CharField(max_length=64, null=False, blank=False)
    host = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return f'Player(id={self.id}, display_name={self.display_name!r}, host={self.host!r})'

    def __str__(self):
        return self.display_name
