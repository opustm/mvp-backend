from django.contrib import admin
from main.models import User, Clique, Event, SoloEvent, Invitation, TimeFrame, Schedule, Announcement, Reaction, DirectMessage, CliqueMessage, ToDo, Request


admin.site.register(User)
admin.site.register(Clique)
admin.site.register(Event)
admin.site.register(SoloEvent)
admin.site.register(Schedule)
admin.site.register(TimeFrame)
admin.site.register(Invitation)
admin.site.register(Announcement)
admin.site.register(Reaction)
admin.site.register(DirectMessage)
admin.site.register(CliqueMessage)
admin.site.register(ToDo)
admin.site.register(Request)