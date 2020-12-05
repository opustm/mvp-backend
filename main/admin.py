from django.contrib import admin
from main.models import User, OpusTeam, Event, Invitation, ScheduleTimeFrame


admin.site.register(User)
admin.site.register(OpusTeam)
admin.site.register(Event)
admin.site.register(ScheduleTimeFrame)
admin.site.register(Invitation)