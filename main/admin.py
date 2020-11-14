from django.contrib import admin
from main.models import User, Team, Event, WeeklyAvailability, Invitation


admin.site.register(User)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(WeeklyAvailability)
admin.site.register(Invitation)