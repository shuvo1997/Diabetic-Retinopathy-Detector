from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('submit-report',submit_report),
    path('success', success, name = 'success'),
    path('all-reports', doctor_view_all_reports)
]