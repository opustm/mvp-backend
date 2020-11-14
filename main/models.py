from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.fields import BooleanField
from django.db.models.fields import related


class User(AbstractUser):
    picture = models.CharField(max_length=100, default='pic1')
    theme = models.CharField(max_length=100, default='theme1')
    phone = models.CharField(max_length=100, default='123-456-7890')

class Team(Group):
    picture = models.CharField(max_length=100, default='pic1')
    announcement = models.CharField(max_length=100, default='This is a group')
    invited = models.ManyToManyField(User, related_name='team_invited')
    members = models.ManyToManyField(User, related_name='members')

class Event(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_event')#ONE TEAM HAS MANY EVENTS (ONE2ONE)
    name = models.CharField(max_length=100, default='event')
    start = models.DateTimeField()
    end = models.DateTimeField()
    details = models.CharField(max_length=100, default='event details')
    invited = models.ManyToManyField(User, related_name='event_invited')
    not_going = models.ManyToManyField(User, related_name='not_going')
    details = models.CharField(max_length=100, default='This event is blah blah blah..')
    picture = models.CharField(max_length=100, default='pic1')
    def __str__(self):
        return self.name

# class EventNotes(models.Model):
#     note_poster=models.ManyToManyField(User, on_delete=models.CASCADE)
#     details = models.CharField(max_length=100, default='This event was so fun blah..')
#     picture = models.CharField(max_length=100, default='pic1')

class DayAvailability(models.Model):
    available=BooleanField()
    midnight=BooleanField()
    one=BooleanField()
    two=BooleanField()
    three=BooleanField()
    four=BooleanField()
    five=BooleanField()
    six=BooleanField()
    seven=BooleanField()
    eight=BooleanField()
    nine=BooleanField()
    ten=BooleanField()
    eleven=BooleanField()
    noon=BooleanField()
    pone=BooleanField()
    ptwo=BooleanField()
    pthree=BooleanField()
    pfour=BooleanField()
    pfive=BooleanField()
    psix=BooleanField()
    pseven=BooleanField()
    peight=BooleanField()
    pnine=BooleanField()
    pten=BooleanField()
    peleven=BooleanField()
    def __str__(self):
        return self.available

class WeekAvailability(models.Model):
    user = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='user_availability')#ONE USER HAS MANY WEEK AVAILABILITIES
    week=models.DateField()
    sunday = models.OneToOneField(DayAvailability, on_delete=models.CASCADE, related_name='sunday')
    monday = models.OneToOneField(DayAvailability, on_delete=models.CASCADE,related_name='monday')
    tuesday = models.OneToOneField(DayAvailability, on_delete=models.CASCADE,related_name='tuesday')
    wednesday = models.OneToOneField(DayAvailability, on_delete=models.CASCADE,related_name='wednesday')
    thursday = models.OneToOneField(DayAvailability, on_delete=models.CASCADE,related_name='thursday')
    friday = models.OneToOneField(DayAvailability, on_delete=models.CASCADE,related_name='friday')
    saturday = models.OneToOneField(DayAvailability, on_delete=models.CASCADE,related_name='saturday')
    def __str__(self):
        return self.week

