from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
# this is an edit
def index(request):
    context = {}
    return render(request, 'profiles/index.html', context)

def BiodataViews(request):
    form = BiodataForm()
    if request.method == 'POST':
        form = BiodataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}        
    return render(request,  'profiles/Bio-form.html', context)


def EmploymentDetails(request):
    form = EmploymentDetailsForm()
    if request.method == 'POST':
        form = EmploymentDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}        
    return render(request,  'profiles/employ-form.html', context)            

        

