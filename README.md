## Home to the opus-tm Django REST API: [API](https://opustm-api.herokuapp.com/)
## This API serves our React Web App: [OpusTm](https://opustm.herokuapp.com/)

# Endpoints:
## User
- /addUsers/
- /users/
- /users/&lt;userId&gt;/
- /userDetails/&lt;userName&gt;/
## Team
- /teams/
- /teams/&lt;teamId&gt;/
- /teamDetails/&lt;teamName&gt;/
- /teamMembers/&lt;teamName&gt;/
## Clique
- /cliques/
- /cliques/&lt;cliqueId&gt;/
- /cliqueDetails/&lt;cliqueName&gt;/
- /cliqueMembers/&lt;cliqueName&gt;/
## Invitation
- /invitations/
- /invitation/&lt;invitationId&gt;/
- /invitationDetails/&lt;code&gt;/
## Event
- /events/
- /events/&lt;teamEventId&gt;/
- /cliqueEvents/&lt;cliqueName&gt;/
- /soloEvents/
- /soloEvents/&lt;userEventId&gt;/
- /userSoloEvents/&lt;username&gt;/
## Schedule
- /schedules/
- /schedules/&lt;scheduleId&gt;/
- /userSchedules/&lt;username&gt;/
- /timeframes/
- /timeframes/&lt;timeFrameId&gt;/
- /scheduleTimeFrames/&lt;scheduleId&gt;/
## Announcement
- /announcements/
- /announcements/&lt;announcementId&gt;/
- /cliqueAnnouncements/&lt;cliqueName&gt;/

## DEPLOYMENT: 
For now we have stuck to Heroku for the sake of familiarity. Future plans possibly include deplyment on AWS. To ensure that we always have a working build, we also deploy a staging build to use in development:
[Staging Build](https://opustm-api-staging.herokuapp.com/)

## DATABASE: 
PostgreSQL. We mainly decided on this because of the ease of access with Heroku. However, we are also able to configure Django to run SQLite when testing locally. The pros and cons of each are described well in this [article](https://tableplus.com/blog/2018/08/sqlite-vs-postgresql-which-database-to-use-and-why.html)

## DJANGO MODEL & DIAGRAM: 
Django enables the creation of database model objects in python. Once each model is created, Django automatically creates migrations in which it can create, update, and generate SQL to add to the database based on the python models. The structure of the database is depicted in model.py:

```
class User(AbstractUser):
    picture = models.CharField(max_length=100, default='pic1')
    theme = models.CharField(max_length=100, default='theme1')
    phone = models.CharField(max_length=100, default='123-456-7890')

class Team(Group):
    picture = models.CharField(max_length=100, default='pic1')
    announcement = models.CharField(max_length=100, default='This is a team')
    members = models.ManyToManyField(User, related_name='members')

class Invitation(models.Model):#will need to delete each row once invitee_email joins team
    team =models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_invitation')#ONE TEAM HAS MANY INVITATIONS (ONE2ONE)
    inviter=models.ForeignKey(User, on_delete=models.CASCADE, related_name='inviter')
    invitee_email=models.CharField(max_length=100, default='vansjo01@luther.edu')
    date_invited=models.DateTimeField()

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

class WeeklyAvailability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_availability')#ONE USER HAS MANY WEEK AVAILABILITIES
    week=models.DateTimeField()
    available=BooleanField(default=True,null=True)
```

A diagram of this django model as generated by [GraphViz:](http://www.graphviz.org/documentation/)
Diagram to come

## DJANGO-ADMIN: 
Found at the [/admin](https://opustm-api.herokuapp.com/admin) route of the API. After logging into an admin account, a site administrator can easily manage the database tables without the need to write any SQL. Read more [here](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)
  
## JWT: 
Alongside Django REST we also use JSON-Web Token authentication for secure data transfer. We decided to implement this because it has been an IETF standard in the defined by the [RFC7519](https://tools.ietf.org/html/rfc7519) since 2015. 

## CORS/CSRF: 
We set up a white-list to only allow certain clients make requests to the API. This helps to make sure that only our React app will have access to the database.


