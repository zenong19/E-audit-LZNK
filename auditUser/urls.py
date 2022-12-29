from django.urls import path
from . import views

urlpatterns = [
    path('', views.planMenu, name='planMenu'),
    path('plan', views.plan, name='plan'),
    path('plan/<str:code>', views.planEdit, name='planEdit'),
    path('pelaksanaan', views.pelaksanaan, name='pelaksanaan'),
    path('pelaksanaan/<str:code>', views.pelaksanaanEdit, name='pelaksanaanEdit'),
    path('inquiry_menu', views.inquiryMenu, name='inquiryMenu'),
    path('inquiry/<str:code>', views.inquiry, name='inquiry'),
    path('responseMenu', views.responseMenu, name='responseMenu'),
    path('response/<str:code>', views.response, name='response'),
    path('susulanMenu', views.susulanMenu, name='susulanMenu'),
    path('susulan/<str:code>', views.susulan, name='susulan'),
    path('praAudit', views.praAudit, name='praAudit'),
    path('penilaian_risiko', views.riskAssessment, name='riskAssessment'),
    path('memo', views.memo, name='MEMO'),
]