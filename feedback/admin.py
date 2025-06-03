from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'rating', 'status', 'timestamp')
    list_filter = ('course', 'rating', 'status')
    search_fields = ('name', 'course', 'comment')
    readonly_fields = ('timestamp',)
    list_editable = ('status',)
    list_per_page = 20
