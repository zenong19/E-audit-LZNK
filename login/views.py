from django.http import HttpResponse
from django.shortcuts import render, redirect
from adminUser.models import *


# Create your views here.
def login(request):
    allUser = setup_user.objects.order_by('username')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        for user in allUser:
            if username == (user.userid):

                if password == (user.password):
                    request.session['name'] = user.userid
                    request.session['access1'] = user.access1
                    request.session['access2'] = user.access2
                    request.session['access3'] = user.access3
                    request.session['access4'] = user.access4
                    return redirect('access')
                else:
                    html = "<html><body><script>alert('Incorrect username or password'); window.history.back();</script></body></html>" 
                    return HttpResponse(html)

    context = {}
    return render(request, 'login.html', context)

def access(request):
    if request.method == 'POST':
        access = request.POST['access']

        if access == 'admin':
            return redirect('userSetup')

        elif access == 'audit':
            return redirect('praAudit')

        elif access == 'management':
            return redirect('report')

        elif access == 'setup':
            return redirect('auditType')

        else :
            return redirect('login')

    access1 = request.session['access1']
    access2 = request.session['access2']
    access3 = request.session['access3']
    access4 = request.session['access4']

    log = [access1, access2, access3, access4]

    context = {"log":log}
    return render(request, 'access.html', context)