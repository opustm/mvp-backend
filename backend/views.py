from django.http import HttpResponseRedirect, HttpResponse

def documentation(request):
    html = '''
    
    <html>
        <body>
            <h1>Routes</h1>
            <ul><a href="/admin/">/admin/</a> Django admin. Manage the database with an easy to use gui.</ul>
            <ul><a href="/token-auth/">/token-auth/</a> API View that receives a POST with a user's username and password. Returns a JSON Web Token that can be used for authenticated requests.</ul>
            <ul><a href="/main/users/">/main/users/</a> Create a new user. It's called 'UserList' because normally we'd have a get method here too, for retrieving a list of all User objects.</ul>
            <ul><a href="/main/current_user/">/main/current_users/</a> Determine the current user by their token, and return their data</ul>
        </body>
    </html>
    '''
    return HttpResponse(html)