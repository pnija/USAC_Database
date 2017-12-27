from django.contrib import admin

from .models import Director, Promoter, EventType, EventDay, Race, \
    Participant, Event

admin.site.register(Director)
admin.site.register(Promoter)
admin.site.register(EventType)
admin.site.register(EventDay)
admin.site.register(Race)
admin.site.register(Participant)
admin.site.register(Event)
