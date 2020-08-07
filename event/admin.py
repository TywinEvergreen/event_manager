from django.contrib import admin

from .models import Event, EventType


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'creator', 'type', 'date_time_created', 'spending_date_time', 'slug')


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
