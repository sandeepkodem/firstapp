from django.db import models

# Create your models here.


class Patient(models.Model):
    lastname=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    age=models.IntegerField(null=True,default=None,blank=True)
    amount_paid=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=100,null=True)


    def __str__(self):
        return self.firstname+self.lastname


class Clinicaldata(models.Model):
    components=[('hw', 'height/weight'),('heartrate', 'HEARTRATE'),('bloodpressure','BLOODPRESSURE')]
    componentname=models.CharField(choices=components,max_length=20)
    component_value=models.CharField(max_length=20)
    measuredatetime=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)