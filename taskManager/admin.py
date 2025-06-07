from django.contrib import admin

from .models import Task

# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'task_title', 'task_description', 'created_at')  # Show all fields
    search_fields = ('task_title', 'task_description')  # 🔍 Add search box for these fields
    list_filter = ('created_at',)  # 🧮 Add right-side filter by date
    # ordering = ('created_at',)  # ⬇ Sort tasks: newest first
    # list_editable = ('task_title', 'task_description')  # ✏️ Edit title/desc directly in list view
    list_per_page = 10  # 📄 Pagination (optional, default is 100)
