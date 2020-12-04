from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.fields import BooleanField
from django.db.models.fields import related
import datetime

class Team(Group):
    picture = models.CharField(max_length=100, default='pic1')

class User(AbstractUser):
    picture = models.CharField(max_length=100, default='pic1')
    theme = models.CharField(max_length=100, default='theme1')
    phone = models.CharField(max_length=100, default='123-456-7890')
    teams = models.ManyToManyField(Team, related_name='teams')
    # groups = None

class Invitation(models.Model):#will need to delete each row once invitee_email joins team
    team =models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_invitation')#ONE TEAM HAS MANY INVITATIONS (ONE2ONE)
    inviter=models.ForeignKey(User, on_delete=models.CASCADE, related_name='inviter')
    invitee_email=models.CharField(max_length=100, default='asdf@example.com')
    date_invited=models.DateTimeField()
    code=models.CharField(max_length=6, unique=True)
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

class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userEvent')#ONE TEAM HAS MANY EVENTS (ONE2ONE)
    name = models.CharField(max_length=100, default='New Event')
    start = models.DateTimeField()
    end = models.DateTimeField()
    invited = models.ManyToManyField(User, related_name='userEventInvited')
    not_going = models.ManyToManyField(User, related_name='usersNotGoing')
    details = models.CharField(max_length=100, default='This event is blah blah blah..')
    picture = models.CharField(max_length=100, default='pic1')
    def __str__(self):
        return f"{self.name} for user: {self.user}"

class ScheduleTimeFrame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scheduletimeframeuser')
    team = models.ManyToManyField(Team, related_name='scheduletimeframeteams')
    weekday = models.CharField(max_length=15, choices=[("sunday","SUNDAY"), ("monday","MONDAY"), ("tuesday","TUESDAY"), ("wednesday","WEDNESDAY"), ("thursday","THURSDAY"), ("friday","FRIDAY"), ("saturday","SATURDAY")], default=("sunday","SUNDAY"))
    start = models.TimeField()
    end = models.TimeField()
    def __str__(self):
        return f'{self.user}\'s typical schedule for {self.team} on {self.weekday}. Available from {self.start} to {self.end}.'

class Announcement(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teamevent')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_announcement')
    announcement = models.CharField(max_length=100, default='This is a reminder to do your hw')
    def __str__(self):
        return f'{self.team}: {self.announcement} with event {self.event}'

