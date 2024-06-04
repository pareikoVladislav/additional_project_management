from django.contrib import admin
from management_app.models import Project, Task, Tag

#
# Настройте отображение моделей Project, Task, Tag в админ-панели. Реализуйте следующие возможности:
#
# Поиск по названию задачи для модели Task.
# Поиск по названию проекта для модели Project.
# У модели Task в Админ-панели должны отображаться поля:
# Название задачи
# Проект
# Статус
# Приоритетность
# Дата создания
# Дата сдачи задачи (due_date)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'project', 'status', 'priority', 'created_date', 'due_date']



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...