from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import Patient_Report

# Create your views here.
def home(request):
    return render(request, 'home.html')

def doctor_view_all_reports(request):
    if request.method == 'GET':
        reports = Patient_Report.objects.all()
        return render(request, 'doctor-view-reports.html',context= {'reports': reports})

def submit_report(request):
	if request.method == 'POST':
		form = PatientForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = PatientForm()
	return render(request, 'report-submit.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')
