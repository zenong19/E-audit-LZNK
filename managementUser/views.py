from django.http import HttpResponse
from django.shortcuts import render, redirect
from auditUser.models import *


# Create your views here.
def report(request):
    log = pelaksanaan_audit.objects.all()

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'management/report.html', context)