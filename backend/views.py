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
                <li><a href="/users/1/">/user/&lt;userId&gt;/</a></li>
                <li><a href="/user/asdf/">/user/&lt;userName&gt;/</a></li>
            </ul>
            <h3>Team</h3>
            <ul>
                <li><a href="/teams/">/teams/</a></li>
                <li><a href="/teams/1/">/team/&lt;teamId&gt;/</a></li>
                <li><a href="/team/FlatEarthers/">/team/&lt;teamName&gt;/</a></li>
                <li><a href="/teamMembers/FlatEarthers/">/teamMembers/&lt;teamName&gt;/</a></li>
            </ul>
            <h3>Invitation</h3>
            <ul>
                <li><a href="/invitations/">/invitations/</a></li>
                <li><a href="/invitations/1/">/invitation/&lt;invitationId&gt;/</a></li>
                <li><a href="/invitation/abc123/">/invitation/&lt;invitationCode&gt;/</a></li>
            </ul>
            <h3>Event</h3>
            <ul>
                <li><a href="/events/">/events/</a></li>
                <li><a href="/events/1/">/events/&lt;eventId&gt;/</a></li>
            </ul>
        </body>
    </html>
    '''
    return HttpResponse(html)