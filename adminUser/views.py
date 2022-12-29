from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def userSetup(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        username = request.POST['username']
        password = request.POST['password']
        gender = request.POST['gender']
        email = request.POST['email']
        contact = request.POST['contact']
        try:
            access1 = request.POST['access1']
        except MultiValueDictKeyError:
            access1 = ''
        try:
            access2 = request.POST['access2']
        except MultiValueDictKeyError:
            access2 = ''
        try:
            access3 = request.POST['access3']
        except MultiValueDictKeyError:
            access3 = ''
        try:
            access4 = request.POST['access4']
        except MultiValueDictKeyError:
            access4 = ''
        date = request.POST['date']

        print(userid, username, password, gender, email, contact, access1, access2, access3, access4, date)

        try:
            setup_user.objects.get(userid=userid)
            setup_user.objects.filter(userid=userid).update(username=username, password=password, gender=gender, email=email, contact=contact, access1=access1, access2=access2, access3=access3, access4=access4, date=date)
            
        except ObjectDoesNotExist:
            setup_user.objects.create(userid=userid, username=username, password=password, gender=gender, email=email, contact=contact, access1=access1, access2=access2, access3=access3, access4=access4, date=date)

    uname = request.session['name']
    context = {'username': uname}
    return render(request, 'admin/userSetup.html', context)


def reviewAccess(request):
    log = setup_user.objects.order_by('userid')

    if request.method == 'POST':
        username = request.POST['username']

        try:
            print(username)
            setup_user.objects.filter(username=username).delete()
            return redirect('reviewAccess')
        except ObjectDoesNotExist:
            print("Data not received correctly")

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'admin/reviewAccess.html', context)


def userEdit(request, name):
    log = setup_user.objects.all()

    if request.method == 'POST':
        userid = request.POST['userid']
        username = request.POST['username']
        password = request.POST['password']
        gender = request.POST['gender']
        email = request.POST['email']
        contact = request.POST['contact']
        try:
            access1 = request.POST['access1']
        except MultiValueDictKeyError:
            access1 = ''
        try:
            access2 = request.POST['access2']
        except MultiValueDictKeyError:
            access2 = ''
        try:
            access3 = request.POST['access3']
        except MultiValueDictKeyError:
            access3 = ''
        try:
            access4 = request.POST['access4']
        except MultiValueDictKeyError:
            access4 = ''
        date = request.POST['date']

        try:
            setup_user.objects.get(userid=userid)
            setup_user.objects.filter(userid=userid).update(username=username, password=password, gender=gender, email=email, contact=contact, access1=access1, access2=access2, access3=access3, access4=access4, date=date)
            
        except ObjectDoesNotExist:
            setup_user.objects.create(userid=userid, username=username, password=password, gender=gender, email=email, contact=contact, access1=access1, access2=access2, access3=access3, access4=access4, date=date)

        return redirect('userSetup')

    uname = request.session['name']
    context = {'username': uname, 'log':log, 'name':name}
    return render(request, 'admin/userEdit.html', context)
