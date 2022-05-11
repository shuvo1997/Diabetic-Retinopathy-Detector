from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('submit-report',submit_report, name = 'submit_report'),
    path('success', success, name = 'success'),
    path('all-reports', doctor_view_all_reports, name = 'all_reports'),
    path('generate-report', generate_report, name='generate_report'),
    
]