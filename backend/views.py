from django.http import HttpResponseRedirect, HttpResponse

def documentation(request):
    html = '''
    
    <html>
        <head>
            <title>OpusAPI</title>
        </head>
        <body>
            <p><a href="/admin/">/admin/</a> Django admin. Manage the database with a user friendly gui.</p>
            <a href="/tokenAuth/">/tokenAuth/</a> API View that receives a POST with a user's username and password. Returns a JSON Web Token that can be used for authenticated requests.

            <h1>Views</h1>
            <h3>User</h3>
            <ul>
                <li><a href="/currentUser/">/currentUser/</a></li>
                <li><a href="/addUsers/">/addUsers/</a></li>
                <li><a href="/users/">/users/</a></li>
                <li><a href="/users/4/">/users/&lt;userId&gt;/</a></li>
                <li><a href="/userDetails/barackO/">/userDetails/&lt;userName&gt;/</a></li>
            </ul>
            <h3>Clique</h3>
            <ul>
                <li><a href="/cliques/">/cliques/</a></li>
                <li><a href="/cliques/1/">/cliques/&lt;cliqueId&gt;/</a></li>
                <li><a href="/cliqueDetails/Poodle People/">/cliqueDetails/&lt;cliqueName&gt;/</a></li>
                <li><a href="/cliqueMembers/Poodle People/">/cliqueMembers/&lt;cliqueName&gt;/</a></li>
            </ul>
            <h3>Invitation</h3>
            <ul>
                <li><a href="/invitations/">/invitations/</a></li>
                <li><a href="/invitations/1/">/invitation/&lt;invitationId&gt;/</a></li>
                <li><a href="/invitationDetails/abc123/">/invitationDetails/&lt;inviteeEmail&gt;/</a></li>
            </ul>
            <h3>Event</h3>
            <ul>
                <li><a href="/events/">/events/</a></li>
                <li><a href="/events/1/">/events/&lt;cliqueEventId&gt;/</a></li>
                <li><a href="/cliqueEvents/Dog Lovers/">/cliqueEvents/&lt;cliqueName&gt;/</a></li>
                <li><a href="/soloEvents/">/soloEvents/</a></li>
                <li><a href="/soloEvents/1/">/soloEvents/&lt;userEventId&gt;/</a></li>
                <li><a href="/userSoloEvents/barackO/">/userSoloEvents/&lt;username&gt;/</a></li>
            </ul>
            <h3>Schedule</h3>
            <ul>
                <li><a href="/schedules/">/schedules/</a></li>
                <li><a href="/schedules/1/">/schedules/&lt;scheduleId&gt;/</a></li>
                <li><a href="/userSchedules/barackO/">/userSchedules/&lt;username&gt;/</a></li>
                <li><a href="/timeFrames/">/timeframes/</a></li>
                <li><a href="/timeFrames/1/">/timeframes/&lt;timeFrameId&gt;/</a></li>
                <li><a href="/scheduleTimeFrames/1/">/scheduleTimeFrames/&lt;scheduleId&gt;/</a></li>
            </ul>
            <h3>Announcement</h3>
            <ul>
                <li><a href="/announcements/">/announcements/</a></li>
                <li><a href="/announcements/1/">/announcements/&lt;announcementId&gt;/</a></li>
                <li><a href="/cliqueAnnouncements/Dog Lovers/">/cliqueAnnouncements/&lt;cliqueName&gt;/</a></li>
            </ul>
        </body>
    </html>
    '''
    return HttpResponse(html)
