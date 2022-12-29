from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from setupUser.models import *
from adminUser.models import *
from .models import *

# Create your views here.
def planMenu(request):
    log = perancangan_audit.objects.order_by('code')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'audit/planMenu.html', context)


def plan(request):
    pa = perancanganAudit.objects.all()
    j = jenis.objects.all()
    p = pp.objects.all()
    e = elemen.objects.all()
    dept = jabatanAuditi.objects.all()
    staff = kumpulanAudit.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        try:
            plan = request.POST['plan']
        except MultiValueDictKeyError:
            plan = ''
        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''
        try:
            pengauditan = request.POST['pengauditan']
        except MultiValueDictKeyError:
            pengauditan = ''
        try:
            e = request.POST['elemen']
        except MultiValueDictKeyError:
            e = ''
        try:
            indicator = request.POST['indicator']
        except MultiValueDictKeyError:
            indicator = ''
        try:
            subIndicator = request.POST['subIndicator']
        except MultiValueDictKeyError:
            subIndicator = ''
        try:
            department = request.POST['department']
        except MultiValueDictKeyError:
            department = ''
        try:
            auditor = request.POST['auditor']
        except MultiValueDictKeyError:
            auditor = ''
        try:
            f = request.POST['from']
        except MultiValueDictKeyError:
            f = ''
        try:
            t = request.POST['to']
        except MultiValueDictKeyError:
            t = ''

        print(code, plan, type, pengauditan, elemen, subIndicator, department, auditor, f, t)

        try:
            perancangan_audit.objects.get(code=code)
            perancangan_audit.objects.filter(code=code).update(plan=plan, type=type, pengauditan=pengauditan, elemen=e, subIndicator=subIndicator, department=department, auditor=auditor, f=f, t=t)
            
        except ObjectDoesNotExist:
            perancangan_audit.objects.create(code=code, plan=plan, type=type, pengauditan=pengauditan, elemen=elemen, subIndicator=subIndicator, department=department, auditor=auditor, f=f, t=t)
        
        return redirect('planMenu')

    uname = request.session['name']
    context = {'username': uname, 'j':j, 'pa':pa, 'p':p, 'e':e, 'dept':dept, 'staff':staff}
    return render(request, 'audit/plan.html', context)


def planEdit(request, code):
    log = perancangan_audit.objects.order_by('code')
    j = jenis.objects.all()
    pa = perancanganAudit.objects.all()
    p = pp.objects.all()
    e = elemen.objects.all()
    dept = jabatanAuditi.objects.all()
    staff = kumpulanAudit.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        try:
            plan = request.POST['plan']
        except MultiValueDictKeyError:
            plan = ''
        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''
        try:
            pengauditan = request.POST['pengauditan']
        except MultiValueDictKeyError:
            pengauditan = ''
        try:
            e = request.POST['elemen']
        except MultiValueDictKeyError:
            e = ''
        try:
            indicator = request.POST['indicator']
        except MultiValueDictKeyError:
            indicator = ''
        try:
            subIndicator = request.POST['subIndicator']
        except MultiValueDictKeyError:
            subIndicator = ''
        try:
            department = request.POST['department']
        except MultiValueDictKeyError:
            department = ''
        try:
            auditor = request.POST['auditor']
        except MultiValueDictKeyError:
            auditor = ''
        try:
            f = request.POST['from']
        except MultiValueDictKeyError:
            f = ''
        try:
            t = request.POST['to']
        except MultiValueDictKeyError:
            t = ''
        try:
            status = request.POST['status']
        except MultiValueDictKeyError:
            status = ''

        print(code, plan, type, pengauditan, e, indicator, subIndicator, department, auditor, f, t, status)

        try:
            perancangan_audit.objects.get(code=code)
            perancangan_audit.objects.filter(code=code).update(plan=plan, type=type, pengauditan=pengauditan, elemen=e, subIndicator=subIndicator, department=department, auditor=auditor, f=f, t=t, status=status)
            
        except ObjectDoesNotExist:
            perancangan_audit.objects.create(code=code, plan=plan, type=type, pengauditan=pengauditan, elemen=elemen, subIndicator=subIndicator, department=department, auditor=auditor, f=f, t=t, status=status)

        return redirect('planMenu')

    uname = request.session['name']
    context = {'username': uname, 'code':code, 'log':log, 'j':j, 'pa':pa, 'p':p, 'e':e, 'dept':dept, 'staff':staff}
    return render(request, 'audit/planEdit.html', context)


def pelaksanaan(request):
    log = perancangan_audit.objects.order_by('code')
    kriteria = senaraiSemak.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        try:
            plan = request.POST['plan']
        except MultiValueDictKeyError:
            plan = ''
        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''
        try:
            pengauditan = request.POST['pengauditan']
        except MultiValueDictKeyError:
            pengauditan = ''
        try:
            elemen = request.POST['elemen']
        except MultiValueDictKeyError:
            elemen = ''
        try:
            indicator = request.POST['indicator']
        except MultiValueDictKeyError:
            indicator = ''
        try:
            subIndicator = request.POST['subIndicator']
        except MultiValueDictKeyError:
            subIndicator = ''
        try:
            auditor = request.POST['auditor']
        except MultiValueDictKeyError:
            auditor = ''
        try:
            f = request.POST['from']
        except MultiValueDictKeyError:
            f = ''
        try:
            t = request.POST['to']
        except MultiValueDictKeyError:
            t = ''
        try:
            status = request.POST['status']
        except MultiValueDictKeyError:
            status = ''
        try:
            criteria = request.POST['criteria']
        except MultiValueDictKeyError:
            criteria = ''
        

        # print(code, plan, type, pengauditan, indicator, subIndicator, auditor, f, t, status, criteria)

        try:
            pelaksanaan_audit.objects.get(code=code)
            pelaksanaan_audit.objects.filter(code=code).update(plan=plan, type=type, pengauditan=pengauditan, elemen=elemen, subIndicator=subIndicator, auditor=auditor, criteria=criteria, status=status, f=f, t=t)
            
        except ObjectDoesNotExist:
            pelaksanaan_audit.objects.create(code=code, plan=plan, type=type, pengauditan=pengauditan, elemen=elemen, subIndicator=subIndicator, auditor=auditor, criteria=criteria, status=status, f=f, t=t)

        return redirect('inquiryMenu')

    uname = request.session['name']
    context = {'username': uname, 'log':log, 'kriteria':kriteria}
    return render(request, 'audit/pelaksanaan.html', context)


def pelaksanaanEdit(request, code):
    log = perancangan_audit.objects.order_by('code')
    kriteria = senaraiSemak.objects.all()
    e = elemen.objects.all()
    i = indikator.objects.all()
    subindikator = subIndikator.objects.all()
    staff = kumpulanAudit.objects.all()
    p = pp.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        try:
            plan = request.POST['plan']
        except MultiValueDictKeyError:
            plan = ''
        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''
        try:
            pengauditan = request.POST['pengauditan']
        except MultiValueDictKeyError:
            pengauditan = ''
        try:
            e = request.POST['elemen']
        except MultiValueDictKeyError:
            e = ''
        try:
            indicator = request.POST['indicator']
        except MultiValueDictKeyError:
            indicator = ''
        try:
            subIndicator = request.POST['subIndicator']
        except MultiValueDictKeyError:
            subIndicator = ''
        try:
            auditor = request.POST['auditor']
        except MultiValueDictKeyError:
            auditor = ''
        try:
            f = request.POST['from']
        except MultiValueDictKeyError:
            f = ''
        try:
            t = request.POST['to']
        except MultiValueDictKeyError:
            t = ''
        try:
            status = request.POST['status']
        except MultiValueDictKeyError:
            status = ''
        try:
            criteria = request.POST['criteria']
        except MultiValueDictKeyError:
            criteria = ''
        

        # print(code, plan, type, pengauditan, indicator, subIndicator, auditor, f, t, status, criteria)

        try:
            pelaksanaan_audit.objects.filter(code=code).get(elemen=e)
            print("Found")
            # pelaksanaan_audit.objects.filter(code=code).update(plan=plan, type=type, pengauditan=pengauditan, elemen=e, subIndicator=subIndicator, auditor=auditor, criteria=criteria, status=status, f=f, t=t)
            
        except ObjectDoesNotExist:
            print("NOT Found")
            pelaksanaan_audit.objects.create(code=code, plan=plan, type=type, pengauditan=pengauditan, elemen=e, subIndicator=subIndicator, auditor=auditor, criteria=criteria, status=status, f=f, t=t)

        return redirect('inquiryMenu')

    uname = request.session['name']
    context = {'username': uname, 'log':log, 'kriteria':kriteria, 'e':e, 'i':i, 'subindikator':subindikator, 'staff':staff, 'p':p, 'code':code}
    return render(request, 'audit/pelaksanaanEdit.html', context)


def inquiryMenu(request):
    log = pelaksanaan_audit.objects.order_by('code')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'audit/inquiryMenu.html', context)


def inquiry(request, code):
    log = pelaksanaan_audit.objects.order_by('code')
    kriteria = senaraiSemak.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        try:
            plan = request.POST['plan']
        except MultiValueDictKeyError:
            plan = ''
        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''
        try:
            pengauditan = request.POST['pengauditan']
        except MultiValueDictKeyError:
            pengauditan = ''
        try:
            elemen = request.POST['elemen']
        except MultiValueDictKeyError:
            elemen = ''
        try:
            indicator = request.POST['indicator']
        except MultiValueDictKeyError:
            indicator = ''
        try:
            subIndicator = request.POST['subIndicator']
        except MultiValueDictKeyError:
            subIndicator = ''
        try:
            auditor = request.POST['auditor']
        except MultiValueDictKeyError:
            auditor = ''
        try:
            status = request.POST['status']
        except MultiValueDictKeyError:
            status = ''
        try:
            criteria = request.POST['criteria']
        except MultiValueDictKeyError:
            criteria = ''
        try:
            att = request.POST['att']
        except MultiValueDictKeyError:
            att = ''
        try:
            catatan = request.POST['catatan']
        except MultiValueDictKeyError:
            catatan = ''

        print(code, plan, type, pengauditan, indicator, subIndicator, auditor, criteria, status, att, catatan)

        try:
            pemerhatian_audit.objects.get(code=code)
            pemerhatian_audit.objects.filter(code=code).update(plan=plan, type=type, pengauditan=pengauditan, elemen=elemen, subIndicator=subIndicator, auditor=auditor, criteria=criteria, status=status, att=att, catatan=catatan)
            
        except ObjectDoesNotExist:
            pemerhatian_audit.objects.create(code=code, plan=plan, type=type, pengauditan=pengauditan, elemen=elemen, subIndicator=subIndicator, auditor=auditor, criteria=criteria, status=status, att=att, catatan=catatan)

        return redirect('responseMenu')

    uname = request.session['name']
    context = {'username': uname, 'log':log, 'kriteria':kriteria, 'code':code}
    return render(request, 'audit/inquiry.html', context)


def responseMenu(request):
    log = pemerhatian_audit.objects.order_by('code')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'audit/responseMenu.html', context)


def response(request, code):
    log = pemerhatian_audit.objects.order_by('code')
    kriteria = senaraiSemak.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        try:
            plan = request.POST['plan']
        except MultiValueDictKeyError:
            plan = ''
        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''
        try:
            pengauditan = request.POST['pengauditan']
        except MultiValueDictKeyError:
            pengauditan = ''
        try:
            elemen = request.POST['elemen']
        except MultiValueDictKeyError:
            elemen = ''
        try:
            indicator = request.POST['indicator']
        except MultiValueDictKeyError:
            indicator = ''
        try:
            subIndicator = request.POST['subIndicator']
        except MultiValueDictKeyError:
            subIndicator = ''
        try:
            auditor = request.POST['auditor']
        except MultiValueDictKeyError:
            auditor = ''
        try:
            status = request.POST['status']
        except MultiValueDictKeyError:
            status = ''
        try:
            criteria = request.POST['criteria']
        except MultiValueDictKeyError:
            criteria = ''
        try:
            att = request.POST['att']
        except MultiValueDictKeyError:
            att = ''
        try:
            marks = request.POST['marks']
        except MultiValueDictKeyError:
            marks = ''
        try:
            catatan = request.POST['catatan']
        except MultiValueDictKeyError:
            catatan = ''

        # print(code, plan, type, pengauditan, indicator, subIndicator, auditor, criteria, status, att, marks, catatan)

        try:
            maklumbalas_audit.objects.get(code=code)
            maklumbalas_audit.objects.filter(code=code).update(plan=plan, type=type, pengauditan=pengauditan, elemen=elemen, subIndicator=subIndicator, auditor=auditor, criteria=criteria, status=status, catatan=catatan, att=att, marks=marks)
            
        except ObjectDoesNotExist:
            maklumbalas_audit.objects.create(code=code, plan=plan, type=type, pengauditan=pengauditan, elemen=elemen, subIndicator=subIndicator, auditor=auditor, criteria=criteria, status=status, catatan=catatan, att=att, marks=marks)
        
        return redirect('susulanMenu')

    uname = request.session['name']
    context = {'username': uname, 'log':log, 'kriteria':kriteria, 'code':code}
    return render(request, 'audit/response.html', context)


def susulanMenu(request):
    log = maklumbalas_audit.objects.filter(status__icontains="no")

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'audit/susulanMenu.html', context)


def susulan(request, code):
    log = maklumbalas_audit.objects.order_by('code')
    kriteria = senaraiSemak.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        try:
            plan = request.POST['plan']
        except MultiValueDictKeyError:
            plan = ''
        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''
        try:
            pengauditan = request.POST['pengauditan']
        except MultiValueDictKeyError:
            pengauditan = ''
        try:
            indicator = request.POST['indicator']
        except MultiValueDictKeyError:
            indicator = ''
        try:
            subIndicator = request.POST['subIndicator']
        except MultiValueDictKeyError:
            subIndicator = ''
        try:
            auditor = request.POST['auditor']
        except MultiValueDictKeyError:
            auditor = ''
        try:
            status = request.POST['status']
        except MultiValueDictKeyError:
            status = ''
        try:
            criteria = request.POST['criteria']
        except MultiValueDictKeyError:
            criteria = ''
        try:
            att = request.POST['att']
        except MultiValueDictKeyError:
            att = ''
        try:
            marks = request.POST['marks']
        except MultiValueDictKeyError:
            marks = ''
        try:
            catatan = request.POST['catatan']
        except MultiValueDictKeyError:
            catatan = ''

        # print(code, plan, type, pengauditan, indicator, subIndicator, auditor, criteria, status, att, marks, catatan)

        try:
            maklumbalas_audit.objects.get(code=code)
            maklumbalas_audit.objects.filter(code=code).update(plan=plan, type=type, pengauditan=pengauditan, indicator=indicator, subIndicator=subIndicator, auditor=auditor, criteria=criteria, status=status, catatan=catatan, att=att, marks=marks)
            
        except ObjectDoesNotExist:
            maklumbalas_audit.objects.create(code=code, plan=plan, type=type, pengauditan=pengauditan, indicator=indicator, subIndicator=subIndicator, auditor=auditor, criteria=criteria, status=status, catatan=catatan, att=att, marks=marks)
        
        return redirect('responseMenu')

    uname = request.session['name']
    context = {'username': uname, 'log':log, 'kriteria':kriteria, 'code':code}
    return render(request, 'audit/susulan.html', context)


def praAudit(request):
    log = sejarahAudit.objects.order_by('code')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'audit/praAudit.html', context)


def riskAssessment(request):
    j = jenis.objects.all()
    r = risiko.objects.all()
    e = elemen.objects.all()
    i = indikator.objects.all()
    s = subIndikator.objects.all()

    if request.method == 'POST':
        type = request.POST['type']
        risk = request.POST['risk']
        element = request.POST['element']
        indicator = request.POST['indicator']
        subIndicator = request.POST['subIndicator']
        question = request.POST['question']
        Kebarangkalian = request.POST['Kebarangkalian']
        Impak = request.POST['Impak']
        total = request.POST['total']
        level = request.POST['level']

        print(type, risk, element, indicator, subIndicator, question, Kebarangkalian, Impak, total, level)

        try:
            risk_assessment.objects.get(type=type)
            risk_assessment.objects.filter(type=type).update(risk=risk, element=element, indicator=indicator, subIndicator=subIndicator, question=question, Kebarangkalian=Kebarangkalian, Impak=Impak, total=total, level=level)
            
        except ObjectDoesNotExist:
            risk_assessment.objects.create(type=type, risk=risk, element=element, indicator=indicator, subIndicator=subIndicator, question=question, Kebarangkalian=Kebarangkalian, Impak=Impak, total=total, level=level)

    uname = request.session['name']
    context = {'username': uname, 'j':j, 'r':r, 'e':e, 'i':i, 's':s}
    return render(request, 'audit/riskAssessment.html', context)


def memo(request):
    log = setup_user.objects.order_by('id')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'audit/memo.html', context)

