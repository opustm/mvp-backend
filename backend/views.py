from django.http import HttpResponseRedirect, HttpResponse

def documentation(request):
    html = '''
    
    <html>
        <head>
            <title>OpusAPI</title>
        </head>
        <body>
            <p><a href="/admin/">/admin/</a> Django admin. Manage the database with a user friendly gui.</p>
            <a href="/token-auth/">/token-auth/</a> API View that receives a POST with a user's username and password. Returns a JSON Web Token that can be used for authenticated requests.

            <h1>Custom Views</h1>
            <h3>User</h3>
            <ul>
                <li><a href="/users/">/users/</a></li>
                <li><a href="/users/4/">/user/&lt;userId&gt;/</a></li>
                <li><a href="/userByUsername/asdf/">/userByUsername/&lt;userName&gt;/</a></li>
            </ul>
            <h3>Team</h3>
            <ul>
                <li><a href="/teams/">/teams/</a></li>
                <li><a href="/teams/1/">/team/&lt;teamId&gt;/</a></li>
                <li><a href="/teamByTeamname/FlatEarthers/">/teamByTeamname/&lt;teamName&gt;/</a></li>
                <li><a href="/teamMembers/FlatEarthers/">/teamMembers/&lt;teamName&gt;/</a></li>
            </ul>
            <h3>Invitation</h3>
            <ul>
                <li><a href="/invitations/">/invitations/</a></li>
                <li><a href="/invitations/1/">/invitation/&lt;invitationId&gt;/</a></li>
                <li><a href="/invitationByCode/abc123/">/invitationByCode/&lt;invitationCode&gt;/</a></li>
            </ul>
            <h3>Event</h3>
            <ul>
                <li><a href="/events/">/events/</a></li>
                <li><a href="/events/1/">/events/&lt;eventId&gt;/</a></li>
                <li><a href="/teamEventsByTeamname/FlatEarthers/">/teamEventsByTeamname/&lt;teamName&gt;/</a></li>
                <li><a href="/userEvents/">/userEvents/</a></li>
                <li><a href="/userEvents/1/">/events/&lt;userEventId&gt;/</a></li>
                <li><a href="/userEventsByUsername/barackO/">/userEventsByUsername/&lt;username&gt;/</a></li>
            </ul>
            <h3>Schedule</h3>
            <ul>
                <li><a href="/scheduleTimeFrames/">/scheduleTimeFrames/</a></li>
                <li><a href="/scheduleTimeFrames/1/">/scheduleTimeFrames/&lt;scheduleTimeFrameId&gt;/</a></li>
                <li><a href="/usersScheduleTimeFramesByUsername/user0/">/usersScheduleTimeFramesByUsername/&lt;username&gt;/</a></li>
            </ul>
            <h3>Announcement</h3>
            <ul>
                <li><a href="/announcements/">/announcements/</a></li>
                <li><a href="/announcements/1/">/announcements/&lt;announcementId&gt;/</a></li>
                <li><a href="/teamAnnouncementsByUsername/FlatEarthers/">/teamAnnouncementsByUsername/&lt;TeamName&gt;/</a></li>
            </ul>
        </body>
    </html>
    '''
    return HttpResponse(html)