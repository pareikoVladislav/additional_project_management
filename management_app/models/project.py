from django.db import models


# Название проекта: строковое, уникальное
# Описание проекта: строковое, большое поле, обязательно к заполнению
# Дата создания проекта: должна проставляться автоматически при создании


class Project(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        #unique_together = ('name', 'description')
