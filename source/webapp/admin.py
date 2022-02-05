from django.contrib import admin

# Register your models here.
from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
    list_filter = ['question']
    search_fields = ['question']
    fields = ['question', 'creation_date']
    readonly_fields = ['creation_date']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Answer)
