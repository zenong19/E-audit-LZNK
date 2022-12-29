from django.urls import path
from . import views

urlpatterns = [
    path('', views.userSetup, name='userSetup'),
    path('reviewAccess', views.reviewAccess, name='reviewAccess'),
    path('_<str:name>', views.userEdit, name='userEdit'),
]