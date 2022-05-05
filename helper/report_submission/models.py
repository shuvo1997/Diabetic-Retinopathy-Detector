from django.db import models

# Create your models here.
class Patient_Report(models.Model):
    patient_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=20, blank= True, null= True)
    weight = models.IntegerField(blank=True, null= True)
    years_diabetes = models.IntegerField()
    submittedAt = models.DateTimeField(auto_now=True)
    ischecked = models.BooleanField(default=False)
    leftRetina = models.ImageField(upload_to = 'images/')
    rightRetina = models.ImageField(upload_to = 'images/')
