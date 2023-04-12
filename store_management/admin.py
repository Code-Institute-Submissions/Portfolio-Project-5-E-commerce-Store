from django.contrib import admin

from .models import Comment, Newsletter, Contact


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('title', 'user_name', 'content', 'posted_on', 'approved',)

    readonly_fields = ('product',)

    list_filter = ('posted_on', 'approved',)

    actions = ['approve_comments']

    ordering = ('-posted_on',)

    def approve_comments(self, request, queryset):

        queryset.update(approved=True)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('email_address', 'date',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email_address', 'tel_number', 'message', 'sent_on',)

    list_filter = ('sent_on', )