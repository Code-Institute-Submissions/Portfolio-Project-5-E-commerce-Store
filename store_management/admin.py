from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('title', 'user_name', 'content', 'posted_on', 'approved',)

    readonly_fields = ('product',)
