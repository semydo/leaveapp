from django.shortcuts import render,redirect
from .models import *
from .forms import *

# CHECKS FOR GIT

def index(request):
     data = Biodata.objects.all()
     context = {'data':data}
     return render(request, 'home/index.html', context)

     
def BiodataViews(request):
    gend = Gender.objects.all()
    con = Country.objects.all()
    if request.method == 'POST':
        file_number = request.POST.get('file_number',"")
        first_name = request.POST.get('first_name',"")
        last_name = request.POST.get('last_name',"")
        other_name = request.POST.get('other_namer',"")
        date_of_birth = request.POST.get('date_of_birth',"")
        gender = request.POST.get('gender',"")
        nationality = request.POST.get('nationality',"")
        # created_by = request.POST.get(' created_by',"")
        passport = request.FILES.get('passport',"")

        bio = Biodata(file_number=file_number,first_name=first_name,last_name=last_name,other_name=other_name,
                      date_of_birth=date_of_birth,gender=gender, nationality=nationality,passport=passport)
        bio.save()
        return redirect("/") 
    context = {'gend':gend,'con':con}           
    return render(request,  'profiles/Bio-form.html', context)


def EmploymentDetails(request):
    if request.method == 'POST':
        biodata = request.POST.get('biodata',"")
        ministry = request.POST.get('ministry',"")
        directorate = request.POST.get('directorate',"")
        department = request.POST.get('department',"")
        unit = request.POST.get('unit',"")
        designation = request.POST.get('designation',"")
        salary_scale = request.POST.get('salary_scale',"")
        grade = request.POST.get('grade',"")
        step = request.POST.get('step',"")
        ippis_no = request.POST.get('ippis_no',"")

        e_form = EmploymentDetails(biodata=biodata,ministry=ministry,directorate=directorate,department=department,
                                    unit=unit,designation=designation,salary_scale=salary_scale,grade=grade,step=step,ippis_no=ippis_no)
        
        e_form.save()
        return redirect("/")
    #context = {'form':form}        
    return render(request,  'profiles/e_form.html')            

        

