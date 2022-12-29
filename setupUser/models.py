from django.db import models

# Create your models here.
class jenis(models.Model):
    code = models.CharField(max_length=10)
    type = models.CharField(max_length=10)


class risiko(models.Model):
    code = models.CharField(max_length=10)
    risk = models.CharField(max_length=100)
    type = models.CharField(max_length=10, default=None)


class pp (models.Model):
    code = models.CharField(max_length=10)
    p = models.CharField(max_length=100)
    type = models.CharField(max_length=10)


class elemen(models.Model):
    code = models.CharField(max_length=10)
    element = models.CharField(max_length=100)
    pengauditan = models.CharField(max_length=10)


class indikator(models.Model):
    code = models.CharField(max_length=10)
    indicator = models.CharField(max_length=100)
    element = models.CharField(max_length=10)


class subIndikator(models.Model):
    code = models.CharField(max_length=10)
    subIndicator = models.CharField(max_length=100)
    indicator = models.CharField(max_length=10)


class senaraiSemak(models.Model):
    code = models.CharField(max_length=10)
    criteria = models.CharField(max_length=10)
    mark = models.CharField(max_length=10)
    subIndicator = models.CharField(max_length=100)
    prosedur = models.CharField(max_length=1000)


class jabatanAuditi(models.Model):
    code = models.CharField(max_length=10)
    department = models.CharField(max_length=10)


class perancanganAudit(models.Model):
    code = models.CharField(max_length=10)
    programme = models.CharField(max_length=10)
    type = models.CharField(max_length=10,default=None, blank=True, null=True)
    date = models.CharField(max_length=100)


class penemuanAudit(models.Model):
    code = models.CharField(max_length=10)
    outcome = models.CharField(max_length=10)


class jenisBukti(models.Model):
    code = models.CharField(max_length=10)
    evidence = models.CharField(max_length=10)


class kumpulanAudit(models.Model):
    staff = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    date = models.CharField(max_length=10)


class sejarahAudit(models.Model):
    code = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    staff = models.CharField(max_length=10)
    programme = models.CharField(max_length=10)
    pp = models.CharField(max_length=10)
    indicator = models.CharField(max_length=10)
    subIndicator = models.CharField(max_length=10)
    outcome = models.CharField(max_length=10)
    remark = models.CharField(max_length=10)