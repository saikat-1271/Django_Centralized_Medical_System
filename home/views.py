import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from home.forms import *
from home.models import *

# from django.http import HttpResponse


def home(request):
    return render(request,'home/home.html')
    # return HttpResponse('<h1>judhfuiod</h1>')



def about(request):
    return render(request,'home/about.html')


def contact(request):
    return render(request,'home/contact.html')



def dr_login(request):
    return render(request,'home/doctor_login.html')

def pt_login(request):
    return render(request,'home/doctor_login.html')

def mng_login(request):
    return render(request,'home/doctor_login.html')

def mngmnt_show(request):
    a=patient.objects.all()
    b=doctor.objects.all()
    c=admin.objects.all()
    return render(request, 'mngmnt_show.html', {'x':a,'b':b,'c':c})

def dr_show(request):
    a=patient.objects.all()
    return render(request, 'dr_show.html', {'x':a})

def insert_patient(request):
    return render(request,'insert_patient.html')

def insert_pt(request):
    try:
        t=patient()
        t.name = request.POST.get('name')
        t.email = request.POST.get('email')
        t.password = request.POST.get('password')
        t.mob = request.POST.get('mob')
        t.add = request.POST.get('add')
        t.bp = request.POST.get('bp')
        t.case = request.POST.get('case')
        t.weight = request.POST.get('weight')
        t.save()
        return render(request,'insert_patient.html')
    except Exception as e:
        return HttpResponse(e)




def insert_doctor(request):
    return render(request,'insert_doctor.html')

def insert_dr(request):
    try:
        t=doctor()
        t.name = request.POST.get('name')
        t.email = request.POST.get('email')
        t.password = request.POST.get('password')
        t.mob = request.POST.get('mob')
        t.save()
        return render(request,'insert_doctor.html')
    except Exception as e:
        return HttpResponse(e)


    

def insert_admin(request):
    return render(request,'insert_admin.html')

def insert_adm(request):
    try:
        t=admin()
        t.name = request.POST.get('name')
        t.password = request.POST.get('password')
        t.mob = request.POST.get('mob')
        t.save()
        return render(request,'insert_admin.html')
    except Exception as e:
        return HttpResponse(e)
   

def delete_patient(request,id):
    a=patient.objects.get(id=id)
    a.delete()
    return redirect('../mngmnt_show')

def delete_doctor(request,id):
    a=doctor.objects.get(id=id)
    a.delete()
    return redirect('../mngmnt_show')


def edit_doctor(request,id):
    a=doctor.objects.get(id=id)
    return render(request, 'edit_doctor.html',{'t':a})



def edit_patient(request,id):
    a=patient.objects.get(id=id)
    return render(request, 'edit_patient.html',{'t':a})

def encode_pt(request, id):
    a=patient.objects.get(id=id)
    f=uform_pt(request.POST ,instance=a)
    if f.is_valid():
        f.save()
        return redirect('../patient_login')
    return render(request, 'edit_patient.html',{'t':a})

def edit_admin(request,id):
    a=admin.objects.get(id=id)
    return render(request, 'edit_admin.html',{'t':a})




def encode_dr(request, id):
    a=doctor.objects.get(id=id)
    f=uform_dr(request.POST ,instance=a)
    if f.is_valid():
        f.save()
        return redirect('../doctor_login')
    return render(request, 'edit_doctor.html',{'t':a})






def encode_ad(request, id):
    a=admin.objects.get(id=id)
    f=uform_ad(request.POST ,instance=a)
    if f.is_valid():
        f.save()
        return redirect('../admin_login')
    return render(request, 'edit_admin.html',{'t':a})


def admin_login(request):
    return render(request, 'admin_login.html')

def admin_log(request):
    mob=request.POST.get('mob')
    password=request.POST.get('password')
    try:
        t=admin.objects.get(mob=mob,password=password)
        a=patient.objects.all()
        b=doctor.objects.all()
        c=admin.objects.all()
        return render(request, 'mngmnt_show.html', {'x':a,'b':b,'c':c,'t':t})
    except:
        return render(request, 'admin_login.html')
       


def doctor_login(request):
    return render(request, 'doctor_login.html')


def doctor_show(request):
    a=patient.objects.all()
    return render(request, 'doctor_show.html', {'x':a})

def doctor_log(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    try:
        t=doctor.objects.get(email=email,password=password)
        a=patient.objects.all()
        return render(request, 'doctor_show.html', {'x':a,'b':t})
    except:
        return render(request, 'doctor_login.html')
       
    
def patient_login(request):
    return render(request, 'patient_login.html')


def patient_show(request):
    a=patient.objects.all()
    return render(request, 'patient_show.html', {'x':a})

def patient_log(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    try:
        t=patient.objects.get(email=email,password=password)
        c=patient_history.objects.filter(patient_id=t.id)
        return render(request, 'patient_show.html', {'x':t,'y':c})
    except:
        return render(request, 'patient_login.html')
       
def database(request):
    a=patient.objects.all()
    b=doctor.objects.all()
    c=admin.objects.all()
    return render(request, 'database_show.html', {'x':a,'b':b,'c':c})


def pt_history(request,doctor_id,patient_id):
    a=doctor.objects.get(id=doctor_id)
    b=patient.objects.get(id=patient_id)
    c=patient_history.objects.filter(patient_id=patient_id)
    return render(request,'patient_history_view.html', {'dr':a,'pt':b,'h':c})


# def patient_history_insert(request,doctor_id,patient_id):
#     a=doctor.objects.get(id=doctor_id)
#     b=patient.objects.get(id=patient_id)
#     return render(request,'patient_history_view.html', {'dr':a,'pt':b})





def pt_insert_history(request,doctor_id,patient_id):
    try:
        n=patient_history()
        n.patient_id=request.POST.get('patient_id')
        n.doctor_id=request.POST.get('doctor_id')
        n.password=request.POST.get('password')
        n.report=request.POST.get('report')
        n.doctor_name=request.POST.get('doctor_name')
        n.test_done=request.POST.get('test_done')
        n.prescription=request.POST.get('prescription')
        n.medication=request.POST.get('medication')
        n.date=request.POST.get('date')
        n.save()
        t=doctor.objects.get(id=doctor_id)
        a=patient.objects.all()
        return render(request, 'doctor_show.html', {'x':a,'b':t})
        
        # b=patient.objects.get(id=patient_id)
        # return render(request,'patient_history_insert.html', {'dr':a,'pt':b})

        # a=doctor.objects.get(id=doctor_id)
        # b=patient.objects.get(id=patient_id)
        # c=patient_history.objects.filter(patient_id=patient_id)
        # return render(request,'patient_history_view.html', {'dr':a,'pt':b,'h':c})
        
    except Exception as e:
        return HttpResponse(e)

def insert_pt_history_form(request,doctor_id,patient_id):
    a=doctor.objects.get(id=doctor_id)
    b=patient.objects.get(id=patient_id)
    return render(request,'patient_history_insert.html', {'dr':a,'pt':b})

