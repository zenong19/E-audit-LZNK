from django.db import models

# Create your models here.
class perancangan_audit(models.Model):
    code = models.CharField(max_length=100)
    plan = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    pengauditan = models.CharField(max_length=100)
    elemen = models.CharField(max_length=100, default=None, blank=True, null=True)
    indicator = models.CharField(max_length=100)
    subIndicator = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    auditor = models.CharField(max_length=100)
    f = models.CharField(max_length=100)
    t = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default=None, blank=True, null=True)


class pelaksanaan_audit(models.Model):
    code = models.CharField(max_length=100)
    plan = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    pengauditan = models.CharField(max_length=100)
    elemen = models.CharField(max_length=100, default=None, blank=True, null=True)
    indicator = models.CharField(max_length=100)
    subIndicator = models.CharField(max_length=100)
    auditor = models.CharField(max_length=100)
    criteria = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    f = models.CharField(max_length=100)
    t = models.CharField(max_length=100)


class pemerhatian_audit(models.Model):
    code = models.CharField(max_length=100)
    plan = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    pengauditan = models.CharField(max_length=100)
    elemen = models.CharField(max_length=100, default=None, blank=True, null=True)
    indicator = models.CharField(max_length=100)
    subIndicator = models.CharField(max_length=100)
    auditor = models.CharField(max_length=100)
    criteria = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    att = models.CharField(max_length=100)
    catatan = models.CharField(max_length=100)


class maklumbalas_audit(models.Model):
    code = models.CharField(max_length=100)
    plan = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    pengauditan = models.CharField(max_length=100)
    elemen = models.CharField(max_length=100, default=None, blank=True, null=True)
    indicator = models.CharField(max_length=100)
    subIndicator = models.CharField(max_length=100)
    auditor = models.CharField(max_length=100)
    criteria = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    catatan = models.CharField(max_length=100)
    att = models.CharField(max_length=100)
    marks = models.CharField(max_length=100)


class risk_assessment(models.Model):
    type = models.CharField(max_length=100)
    risk = models.CharField(max_length=100)
    pengauditan = models.CharField(max_length=100)
    indicator = models.CharField(max_length=100)
    subIndicator = models.CharField(max_length=100)
    question = models.CharField(max_length=500)
    Kebarangkalian = models.CharField(max_length=100)
    Impak = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    level = models.CharField(max_length=100)