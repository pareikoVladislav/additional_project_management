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
    search_fields = ('name',)

    def replace_spaces_with_underscores(self, request, objects):
        for obj in objects:
            obj.name = obj.name.replace(" ", "_")
            obj.save()
        return objects

    replace_spaces_with_underscores.short_description = 'Replace spaces with underscorses'

    actions = [replace_spaces_with_underscores]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'project', 'assignee', 'status', 'priority', 'created_date', 'due_date')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...

