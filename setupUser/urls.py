from django.urls import path
from . import views

urlpatterns = [
    path('', views.auditType, name='auditType'),
    path('perancangan_audit', views.programme, name='programme'),
    path('program_pengauditan', views.pengauditan, name='pengauditan'),
    path('elemen_kawalan', views.controlElement, name='controlElement'),
    path('indikator', views.indicator, name='indicator'),
    path('sub_indikator', views.subIndicator, name='subIndicator'),
    path('senarai_semak', views.criteria, name='criteria'),
    path('jabatan_auditi', views.department, name='department'),
    path('penemuan_audit', views.outcome, name='outcome'),
    path('jenis_bukti_audit', views.evidence, name='evidence'),
    path('penilaian_risiko', views.risk, name='risk'),
    path('kumpulan_audit', views.team, name='team'),
    path('audit_history', views.history, name='history'),
]