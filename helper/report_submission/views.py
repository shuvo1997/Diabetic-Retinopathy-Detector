from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import Patient_Report

# Create your views here.
def home(request):
    return render(request, 'home.html')

def doctor_view_all_reports(request):
    if request.method == 'GET':
        reports = Patient_Report.objects.all()
        return render(request, 'view-all-reports.html',context= {'reports': reports})

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

import tensorflow as tf
import numpy as np
import cv2
import os
import pandas as pd

data = pd.read_csv("trainLabels.csv")
model = tf.keras.models.load_model("model-vgg19.h5")
image_location = './media/'
files = os.listdir(image_location)
class_list = ['No_DR', 'Mild_DR', 'Moderate_DR', 'Severe_DR', 'Proliferative_DR']
def make_prediction(img_path):
	a_file = os.path.join(image_location, img_path)
	img = cv2.imread(a_file)
	img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img=cv2.resize(img, (300,300))
	# img=img/255.0
	img=np.expand_dims(img, axis=0)
	prediction =model.predict (img, batch_size=1, verbose=0)
	pred=np.argmax(prediction)
	return 'for file '+ a_file+ ' the predicted class is '+ class_list[pred]+ ' with a probability of '+ str(prediction[0][pred])
# print(a_file)
def generate_report(request):
    if request.method == "GET":
        left_img = request.GET['left_img']
        right_img = request.GET['right_img']
        # parts = left_img.split("/")
        # file_name = parts[-1].split(".")
        # rev = file_name[0][::-1]
        # print(rev)
        # count = 0
        # for i in rev:
        #     if i == "_":
        #         print(count)
        #         break
        #     count += 1
        # f = file_name[0][0:len(file_name[0])-count-1]
        # # print(data[f])
        left_message = make_prediction(left_img) 
        right_message = make_prediction(right_img)
        print(left_img)
        print(right_img)
        dic = {"left_message" : left_message, "right_message" : right_message}
        print(dic)
        return JsonResponse(dic)

