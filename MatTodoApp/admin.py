from django.contrib import admin
from MatTodoApp.models import ToDoItem, Category


class ToDoItemAdmin(admin.ModelAdmin):
    list_display=('title', 'dropDeadDate', 'description')
    search_fields= ('title', 'description')

    # Register your models here.
admin.site.register(ToDoItem, ToDoItemAdmin)
admin.site.register(Category)