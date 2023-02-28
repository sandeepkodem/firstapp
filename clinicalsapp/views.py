
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Patient,Clinicaldata
from .forms import PatienForm,ClinicaldataForm,RegisterForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate,login
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request,'clinicalsapp/index.html')

def home(request):
    return render(request,"clinicalsapp/home.html")



class PatientListView(ListView):
    model=Patient
    
   
    
   


  
   

class PatientCreateView(CreateView):
    model=Patient
    success_url = reverse_lazy('clinicals:list')
    fields="__all__"
   


class PatientUpdateView(UpdateView):
    model=Patient
    success_url = reverse_lazy('clinicals:list')
    fields="__all__"


    #def get_success_url(self) -> str:
     #   return reverse('clinicals:home')

class PatientDeleteView(DeleteView):
    model=Patient
    success_url = reverse_lazy('clinicals:list')

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        username=form.cleaned_data.get('username')
        messages.success(request,f'Welcome {username},your account has been registerd successsfully')
        return redirect("/login")
    else:
        form=RegisterForm()
    return render(request,'clinicalsapp/register.html',{'form':form})



def addData(request,**kwargs):
    form=ClinicaldataForm()
    patient=Patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=ClinicaldataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/index')
    return render(request,'clinicalsapp/clinicaldata_form.html',{'form':form,'patient':patient})



def sendmail(request,**kwargs):
    patient=Patient.objects.get(id=kwargs['pk'])
    pt_email=patient.email
    a='sandeep'
    
        
    
    send_mail(
        'sandeep',
        'this is test',
        settings.EMAIL_HOST_USER,
        [pt_email]
    )
    return redirect("/listview")
    