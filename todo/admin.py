from django.contrib import admin

# Register your models here.
from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
    list_filter = ('created_date',)
    search_fields = ('user',)

    class Meta:
        model = Todo
