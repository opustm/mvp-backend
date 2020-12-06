from django.contrib import admin
from main.models import User, OpusTeam, Clique, Event, SoloEvent, Invitation, TimeFrame, Schedule


admin.site.register(User)
admin.site.register(Clique)
admin.site.register(Event)
admin.site.register(SoloEvent)
admin.site.register(Schedule)
admin.site.register(TimeFrame)
admin.site.register(Invitation)