from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def auditType(request):
    log = jenis.objects.all()
    data = {}

    for d in log:
            data[d.code] = d.type

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''

        print(code, type, mode)

        if mode == 'save':
            try:
                jenis.objects.get(code=code)
                jenis.objects.filter(code=code).update(type=type)
                print("Data saved")
            except ObjectDoesNotExist:
                jenis.objects.create(code=code, type=type)
                print("Data not found")
        else:
            try:
                jenis.objects.get(code=code)
                jenis.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('auditType')

    uname = request.session['name']
    context = {'username': uname, 'data':data}
    return render(request, 'setup/auditType.html', context)


def controlElement(request):
    log = elemen.objects.all()
    p = pp.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            element = request.POST['element']
        except MultiValueDictKeyError:
            element = ''
        try:
            pengauditan = request.POST['pp']
        except MultiValueDictKeyError:
            pengauditan = ''

        if mode == 'save':
            try:
                elemen.objects.get(code=code)
                elemen.objects.filter(code=code).update(element=element, pengauditan=pengauditan)
            except ObjectDoesNotExist:
                elemen.objects.create(code=code, element=element, pengauditan=pengauditan)
        else:
            try:
                elemen.objects.get(code=code)
                elemen.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('controlElement')

    uname = request.session['name']
    context = {'username': uname, 'log':log, 'pp':p}
    return render(request, 'setup/controlElement.html', context)


def indicator(request):
    log = indikator.objects.all()
    e = elemen.objects.all()


    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            indicator = request.POST['indicator']
        except MultiValueDictKeyError:
            indicator = ''
        
        try:
            element = request.POST['element']
        except:
            element = ''

        if mode == 'save':
            try:
                indikator.objects.get(code=code)
                indikator.objects.filter(code=code).update(indicator=indicator, element=element)
            except ObjectDoesNotExist:
                indikator.objects.create(code=code, indicator=indicator, element=element)
        else:
            try:
                indikator.objects.get(code=code)
                indikator.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('indicator')

    uname = request.session['name']
    context = {'username': uname, 'log':log, 'e':e}
    return render(request, 'setup/indicator.html', context)


def subIndicator(request):
    log = subIndikator.objects.all()
    i = indikator.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            subIndicator = request.POST['subIndicator']
        except MultiValueDictKeyError:
            subIndicator = ''
        try:
            indicator = request.POST['indicator']
        except MultiValueDictKeyError:
            indicator = ''

        if mode == 'save':
            try:
                subIndikator.objects.get(code=code)
                subIndikator.objects.filter(code=code).update(subIndicator=subIndicator, indicator=indicator)
            except ObjectDoesNotExist:
                subIndikator.objects.create(code=code, subIndicator=subIndicator, indicator=indicator)
        else:
            try:
                subIndikator.objects.get(code=code)
                subIndikator.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('subIndicator')

    uname = request.session['name']
    context = {'username': uname, 'log':log, 'i':i}
    return render(request, 'setup/subIndicator.html', context)


def criteria(request):
    log = senaraiSemak.objects.all()
    s = subIndikator.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            criteria = request.POST['criteria']
        except MultiValueDictKeyError:
            criteria = ''

        try:
            mark = request.POST['mark']
        except MultiValueDictKeyError:
            mark = ''

        try:
            subIndicator = request.POST['subIndicator']
        except MultiValueDictKeyError:
            subIndicator = ''
        
        try:
            prosedur = request.POST['prosedur']
        except MultiValueDictKeyError:
            prosedur = ''

        if mode == 'save':
            try:
                senaraiSemak.objects.get(code=code)
                senaraiSemak.objects.filter(code=code).update(criteria=criteria, subIndicator=subIndicator, mark=mark, prosedur=prosedur)
            except ObjectDoesNotExist:
                senaraiSemak.objects.create(code=code, criteria=criteria, subIndicator=subIndicator, mark=mark, prosedur=prosedur)
        else:
            try:
                senaraiSemak.objects.get(code=code)
                senaraiSemak.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('criteria')

    uname = request.session['name']
    context = {'username': uname, 'log':log, 's':s}
    return render(request, 'setup/criteria.html', context)


def department(request):
    log = jabatanAuditi.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            department = request.POST['department']
        except MultiValueDictKeyError:
            department = ''

        if mode == 'save':
            try:
                jabatanAuditi.objects.get(code=code)
                jabatanAuditi.objects.filter(code=code).update(department=department)
            except ObjectDoesNotExist:
                jabatanAuditi.objects.create(code=code, department=department)
        else:
            try:
                jabatanAuditi.objects.get(code=code)
                jabatanAuditi.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('department')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'setup/department.html', context)


def programme(request):
    log = perancanganAudit.objects.all()
    # type = jenis.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            programme = request.POST['programme']
        except MultiValueDictKeyError:
            programme = ''
        
        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''

        try:
            date = request.POST['date']
        except MultiValueDictKeyError:
            date = ''

        if mode == 'save':
            try:
                perancanganAudit.objects.get(code=code)
                perancanganAudit.objects.filter(code=code).update(programme=programme, type=type, date=date)
            except ObjectDoesNotExist:
                perancanganAudit.objects.create(code=code, programme=programme, type=type, date=date)
        else:
            try:
                perancanganAudit.objects.get(code=code)
                perancanganAudit.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('programme')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'setup/programme.html', context)


def outcome(request):
    log = penemuanAudit.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            outcome = request.POST['outcome']
        except MultiValueDictKeyError:
            outcome = ''

        if mode == 'save':
            try:
                penemuanAudit.objects.get(code=code)
                penemuanAudit.objects.filter(code=code).update(outcome=outcome)
            except ObjectDoesNotExist:
                penemuanAudit.objects.create(code=code, outcome=outcome)
        else:
            try:
                penemuanAudit.objects.get(code=code)
                penemuanAudit.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('outcome')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'setup/outcome.html', context)


def evidence(request):
    log = jenisBukti.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            evidence = request.POST['evidence']
        except MultiValueDictKeyError:
            evidence = ''

        # print(code, criteria, evidence, mode)

        if mode == 'save':
            try:
                jenisBukti.objects.get(code=code)
                jenisBukti.objects.filter(code=code).update(evidence=evidence)
            except ObjectDoesNotExist:
                jenisBukti.objects.create(code=code, evidence=evidence)
        else:
            try:
                jenisBukti.objects.get(code=code)
                jenisBukti.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('evidence')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'setup/evidence.html', context)


def risk(request):
    log = risiko.objects.all()
    # type = jenis.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            risk = request.POST['risk']
        except MultiValueDictKeyError:
            risk = ''

        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''

        print(code, risk, type, mode)

        if mode == 'save':
            try:
                risiko.objects.get(code=code)
                risiko.objects.filter(code=code).update(risk=risk, type=type)
            except ObjectDoesNotExist:
                risiko.objects.create(code=code, risk=risk, type=type)
        else:
            try:
                risiko.objects.get(code=code)
                risiko.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('risk')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'setup/risk.html', context)


def team(request):
    log = kumpulanAudit.objects.all()

    if request.method == 'POST':
        id = request.POST['code']
        mode = request.POST['mode']

        try:
            name = request.POST['name']
        except MultiValueDictKeyError:
            name = ''
        
        try:
            position = request.POST['position']
        except MultiValueDictKeyError:
            position = ''
        
        try:
            date = request.POST['date']
        except MultiValueDictKeyError:
            date = ''

        if mode == 'save':
            try:
                kumpulanAudit.objects.get(staff=id)
                kumpulanAudit.objects.filter(staff=id).update(name=name, position=position, date=date)
            except ObjectDoesNotExist:
                kumpulanAudit.objects.create(staff=id, name=name, position=position, date=date)
        else:
            try:
                kumpulanAudit.objects.get(staff=id)
                kumpulanAudit.objects.filter(staff=id).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('team')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'setup/team.html', context)


def history(request):
    log = sejarahAudit.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            position = request.POST['position']
        except MultiValueDictKeyError:
            position = ''
        
        try:
            date = request.POST['date']
        except MultiValueDictKeyError:
            date = ''

        try:
            staff = request.POST['staff']
        except MultiValueDictKeyError:
            staff = ''

        try:
            programme = request.POST['programme']
        except MultiValueDictKeyError:
            programme = ''

        try:
            pp = request.POST['pp']
        except MultiValueDictKeyError:
            pp = ''

        try:
            indicator = request.POST['indicator']
        except MultiValueDictKeyError:
            indicator = ''
        
        try:
            subIndicator = request.POST['subIndicator']
        except MultiValueDictKeyError:
            subIndicator = ''
        
        try:
            outcome = request.POST['outcome']
        except MultiValueDictKeyError:
            outcome = ''
        
        try:
            remark = request.POST['remark']
        except MultiValueDictKeyError:
            remark = ''

        if mode == 'save':
            try:
                sejarahAudit.objects.get(code=code)
                sejarahAudit.objects.filter(code=code).update(position=position, date=date, staff=staff, programme=programme, pp=pp, indicator=indicator, subIndicator=subIndicator, outcome=outcome, remark=remark)
            except ObjectDoesNotExist:
                sejarahAudit.objects.create(code=code, position=position, date=date, staff=staff, programme=programme, pp=pp, indicator=indicator, subIndicator=subIndicator, outcome=outcome, remark=remark)
        else:
            try:
                sejarahAudit.objects.get(code=code)
                sejarahAudit.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('history')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'setup/auditHistory.html', context)


def pengauditan(request):
    log = pp.objects.all()
    # type = jenis.objects.all()

    if request.method == 'POST':
        code = request.POST['code']
        mode = request.POST['mode']

        try:
            p = request.POST['pp']
        except MultiValueDictKeyError:
            p = ''
        try:
            type = request.POST['type']
        except MultiValueDictKeyError:
            type = ''

        if mode == 'save':
            try:
                pp.objects.get(code=code)
                pp.objects.filter(code=code).update(p=p, type=type)
            except ObjectDoesNotExist:
                pp.objects.create(code=code, p=p, type=type)
        else:
            try:
                pp.objects.get(code=code)
                pp.objects.filter(code=code).delete()
                print("Data Deleted")
            except ObjectDoesNotExist:
                print("Data not found")
        
        return redirect('pengauditan')

    uname = request.session['name']
    context = {'username': uname, 'log':log}
    return render(request, 'setup/pengauditan.html', context)