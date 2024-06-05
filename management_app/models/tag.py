from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.name
