from django.contrib import admin
from main.models import User, Team, Event, Invitation, WeekSchedule, DaySchedule, WeekTimeFrame, DayTimeFrame


admin.site.register(User)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(WeekSchedule)
admin.site.register(WeekTimeFrame)
admin.site.register(DaySchedule)
admin.site.register(DayTimeFrame)
admin.site.register(Invitation)