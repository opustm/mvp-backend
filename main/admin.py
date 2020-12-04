from django.contrib import admin
from main.models import User, Team, Event, Invitation, ScheduleTimeFrame


admin.site.register(User)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(ScheduleTimeFrame)
admin.site.register(Invitation)