from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.fields import BooleanField
from django.db.models.fields import related
import datetime

class Team(Group):
    picture = models.CharField(max_length=100, default='pic1')
    announcement = models.CharField(max_length=100, default='This is a team')

class User(AbstractUser):
    picture = models.CharField(max_length=100, default='pic1')
    theme = models.CharField(max_length=100, default='theme1')
    phone = models.CharField(max_length=100, default='123-456-7890')
    teams = models.ManyToManyField(Team, related_name='teams')
    # groups = None

class Invitation(models.Model):#will need to delete each row once invitee_email joins team
    team =models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_invitation')#ONE TEAM HAS MANY INVITATIONS (ONE2ONE)
    inviter=models.ForeignKey(User, on_delete=models.CASCADE, related_name='inviter')
    invitee_email=models.CharField(max_length=100, default='vansjo01@luther.edu')
    date_invited=models.DateTimeField()
    code=models.CharField(max_length=6, default='abc123')
    def __str__(self):
        return '{} invited to {} by {}'.format(self.invitee_email, self.team, self.inviter)


class Event(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_event')#ONE TEAM HAS MANY EVENTS (ONE2ONE)
    name = models.CharField(max_length=100, default='event')
    start = models.DateTimeField()
    end = models.DateTimeField()
    invited = models.ManyToManyField(User, related_name='event_invited')
    not_going = models.ManyToManyField(User, related_name='not_going')
    details = models.CharField(max_length=100, default='This event is blah blah blah..')
    picture = models.CharField(max_length=100, default='pic1')
    def __str__(self):
        return f"{self.name} for team: {self.team}"

# class EventNotes(models.Model):
#     note_poster=models.ManyToManyField(User, on_delete=models.CASCADE)
#     details = models.CharField(max_length=100, default='This event was so fun blah..')
#     picture = models.CharField(max_length=100, default='pic1')

class TimeFrame(models.Model):
    day = models.ForeignKey(DailyAvailability)
    start = models.DateTimeField()
    end = models.DateTimeField()
    def __str__(self):
        return f'start:{self.start}\nend:{self.end}'

class DailyAvailability(models.Model):
    availableTimeFrames = models.ManyToManyField(TimeFrame, related_name='available_times')
    def __str__(self):
        return f'Available:"{self.available}\n{self.availableTimeFrames}'

class WeeklyAvailability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_availability')#ONE USER HAS MANY WEEK AVAILABILITIES
    week = models.DateField(("Date"), default=datetime.date.today)
    sunday = models.OneToOneField(DailyAvailability, on_delete=models.CASCADE, related_name='sunday')
    monday = models.OneToOneField(DailyAvailability, on_delete=models.CASCADE,related_name='monday')
    tuesday = models.OneToOneField(DailyAvailability, on_delete=models.CASCADE,related_name='tuesday')
    wednesday = models.OneToOneField(DailyAvailability, on_delete=models.CASCADE,related_name='wednesday')
    thursday = models.OneToOneField(DailyAvailability, on_delete=models.CASCADE,related_name='thursday')
    friday = models.OneToOneField(DailyAvailability, on_delete=models.CASCADE,related_name='friday')
    saturday = models.OneToOneField(DailyAvailability, on_delete=models.CASCADE,related_name='saturday')

