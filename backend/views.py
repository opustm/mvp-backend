from django.http import HttpResponseRedirect

def documentation(request):
    return HttpResponseRedirect("/admin")