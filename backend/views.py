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
                <li><a href="/main/users/">/main/users/</a></li>
                <li><a href="/main/user/asdf">/api/users/&lt;userName&gt;</a></li>
            </ul>
            <h3>Team</h3>
            <ul>
                <li><a href="/main/teams/">/main/teams/</a></li>
                <li><a href="/main/team/FlatEarthers/">/main/teams/&lt;teamName&gt;</a></li>
                <li><a href="/main/teamMembers/FlatEarthers">/main/teamMembers/&lt;teamName&gt;</a></li>
            </ul>
            <h3>Invitation</h3>
            <ul>
                <li><a href="/main/invitations/">/main/invitations/</a></li>
                <li><a href="/main/invitation/abc123/">/main/invitations/&lt;invitationCode&gt;</a></li>
            </ul>
            <h3>Event</h3>
            <ul>
                <li><a href="/main/events/">/main/events/</a></li>
                <li><a href="/main/event/1">/main/events/&lt;eventid&gt;</a></li>
            </ul>
        </body>
    </html>
    '''
    return HttpResponse(html)
            # <ul><a href="/main/users/">/main/users/</a> Get all users. Also, create a new user.</ul>
            # <ul><a href="/main/users/1">/main/users/&lt;userid&gt;</a> Get user by primary key(user id).</ul>
            # <ul><a href="/main/teams/">/main/teams/</a> Get all teams. Also, create a new team.</ul>
            # <ul><a href="/main/teams/1">/main/teams/&lt;teamid&gt;</a> Get team by primary key(team id).</ul>
            # <ul><a href="/main/current_user/">/main/current_users/</a> Determine the current user by their token, and return their data</ul>
            # <ul><a href="/main/events/">/main/events/</a> Get and Post events.</ul>
            # <ul><a href="/main/getIdByUsername/user0">/main/getIdByUsername/&lt;username&gt;</a>Get id by username</ul>

            # <p>Objects can be individually accessed using custom attributes that better fit the use-case of each table.</br>
            # This shows that you can query a table with values other than its primary key!</p>

            # <h1>Default View Sets</h1>
            # <p>Objects can be individually accessed using the primary key(id) of each row.</p>
            # <h3>User</h3>
            # <ul>
            #     <li><a href="/api/user/">/api/user/</a>Read(GET) all users. Create(POST) new users</li>
            #     <li><a href="/api/user/1">/api/user/&lt;userid&gt;</a>Get user by id</li>
            # </ul>
            # <h3>Team</h3>
            # <ul>
            #     <li><a href="/api/team/">/api/team/</a>Read(GET) all users. Create(POST) new teams</li>
            #     <li><a href="/api/team/1">/api/team/&lt;teamid&gt;</a>Get Team by id</li>
            # </ul>
            # <h3>Invitation</h3>
            # <ul>
            #     <li><a href="/api/invitation/">/api/invitation/</a>Read(GET) all invitations. Create(POST) new Invitations</li>
            #     <li><a href="/api/invitation/1">/api/invitation/&lt;invitationid&gt;</a>Get invitation by id. Also, Update(PUT), Delete(DELETE)</li>
            # </ul>
            # <h3>Event</h3>
            # <ul>
            #     <li><a href="/api/event/">/api/event/</a>Read(GET) all events. Create(POST) new events</li>
            #     <li><a href="/api/event/1">/api/event/&lt;eventid&gt;</a>Get event by id. Also, Update(PUT), Delete(DELETE)</li>
            # </ul>