from django.contrib import admin
from main.models import User, Team, Event, Invitation, Schedule


admin.site.register(User)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Schedule)
admin.site.register(Invitation)