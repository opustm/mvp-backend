from django.http import HttpResponseRedirect, HttpResponse

def documentation(request):
    html = '''
    
    <html>
        <body>
            <h1>Routes</h1>
            <ul><a href="/admin/">/admin/</a> Django admin. Manage the database with an easy to use gui.</ul>
            <ul><a href="/main/users/">/main/users/</a> Get all users. Also, create a new user.</ul>
            <ul><a href="/main/users/1">/main/users/&lt;userid&gt;</a> Get user by primary key(user id).</ul>
            <ul><a href="/main/teams/">/main/teams/</a> Get all teams. Also, create a new team.</ul>
            <ul><a href="/main/teams/1">/main/teams/&lt;teamid&gt;</a> Get team by primary key(team id).</ul>
            <ul><a href="/token-auth/">/token-auth/</a> API View that receives a POST with a user's username and password. Returns a JSON Web Token that can be used for authenticated requests.</ul>
            <ul><a href="/main/current_user/">/main/current_users/</a> Determine the current user by their token, and return their data</ul>
        </body>
    </html>
    '''
    return HttpResponse(html)