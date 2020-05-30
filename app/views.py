from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Patient
from .forms import *


# Create your views here.
def login(request):
    context = {}
    return render(request, 'login.html', context)


def home(request):
    pat = Patient.objects.all().order_by('-id')
    context = {"pat": pat}
    return render(request, 'home.html', context)


def create(request):
    form = PatientForm()

    form1 = Patient.objects.all()

    if request.method == "POST":
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/app/home/')
    context = {'form': form, 'form1': form1}
    return render(request, 'create.html', context)


def edit(request, pk):
    pat = Patient.objects.get(id=pk)
    form = PatientForm(instance=pat)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=pat)
        if form.is_valid():
            form.save()
            return redirect('/app/home/')
    context = {'form': form}
    return render(request, 'create.html', context)


def submit(request, pk):
    pat = Patient.objects.get(id=pk)
    b = bloodform(instance=pat)
    c=CBCForm(instance=pat)
    u=urineform(instance=pat)
    ur=urineroutineform(instance=pat)
    st=Stoolform(instance=pat)
    semen=semenform(instance=pat)
    res=resultform(instance=pat)
    alkal=alkali(instance=pat)
    f1=HaematologyForm1(instance=pat)
    f2=HaematologyForm2(instance=pat)
    f3=HaematologyForm3(instance=pat)
    f4=HaematologyForm4(instance=pat)
    f5=HaematologyForm5(instance=pat)
    f6=HaematologyForm6(instance=pat)
    ser1=serologyform1(instance=pat)
    ser2=serologyform2(instance=pat)
    ser3=serologyform3(instance=pat)
    ser4=serologyform4(instance=pat)
    ser5=serologyform5(instance=pat)
    ser6=serologyform6(instance=pat)
    ser7=serologyform7(instance=pat)
    bio1=biochemlipidform1(instance=pat)
    bio2=biochemkftform2(instance=pat)
    bio3=biochemlftform3(instance=pat)
    bio4=biochemlftoptionform4(instance=pat)
    bio5=biochemlftoptionform5(instance=pat)
    dan1=dannu1(instance=pat)
    dan2=dannu2(instance=pat)
    dan3=dannu3(instance=pat)
    dan4=dannu4(instance=pat)
    dan5=dannu5(instance=pat)
    dan6=dannu6(instance=pat)


    d1=pat.serumcrea
    d6=pat.Sgot
    d2=pat.Uric_Acid
    d3=pat.Serum_Calcium
    d4=pat.Serum_Sodium
    d5=pat.Serum_Pottasium
    b1=pat.t1
    b2=pat.t2
    b3=pat.t3
    b4=pat.t4
    Cbc=pat.cbc
    U1=pat.u1
    U2=pat.u2
    Ur=pat.ur
    St=pat.st
    sem=pat.semen
    F1=pat.haemoglobin
    F2=pat.bloodgrp
    F3=pat.BT_CT
    F4=pat.TotalCount
    F5=pat.DiffCount
    F6=pat.usr
    sero1 = pat.St1
    sero2 = pat.St2
    sero3 = pat.St3
    sero4 = pat.St4
    sero5 = pat.St5
    sero6 = pat.St6
    sero7 = pat.St7
    alk=pat.AkPh
    B1=pat.blipid
    B2=pat.KFT
    B3=pat.leftest
    B4=pat.Sgpt
    B5=pat.bilirubin
    if request.method == "POST":
        b = bloodform(request.POST, instance=pat)
        c = CBCForm(request.POST, instance=pat)
        u = urineform(request.POST, instance=pat)
        dan1 = dannu1(request.POST, instance=pat)
        dan2 = dannu2(request.POST, instance=pat)
        dan3 = dannu3(request.POST, instance=pat)
        dan4 = dannu4(request.POST, instance=pat)
        dan5 = dannu5(request.POST, instance=pat)
        dan6 = dannu6(request.POST, instance=pat)
        res = resultform(request.POST, instance=pat)
        ur = urineroutineform(request.POST, instance=pat)
        st = Stoolform(request.POST, instance=pat)
        alkal = alkali(request.POST, instance=pat)
        semen = semenform(request.POST,instance=pat)
        f1=HaematologyForm1(request.POST,instance=pat)
        f2=HaematologyForm2(request.POST,instance=pat)
        f3=HaematologyForm3(request.POST,instance=pat)
        f4=HaematologyForm4(request.POST,instance=pat)
        f5=HaematologyForm5(request.POST,instance=pat)
        f6=HaematologyForm6(request.POST,instance=pat)
        ser1=serologyform1(request.POST,instance=pat)
        ser2=serologyform2(request.POST,instance=pat)
        ser3=serologyform3(request.POST,instance=pat)
        ser4=serologyform4(request.POST,instance=pat)
        ser5=serologyform5(request.POST,instance=pat)
        ser6=serologyform6(request.POST,instance=pat)
        ser7=serologyform7(request.POST,instance=pat)
        bio1 = biochemlipidform1(request.POST,instance=pat)
        bio2 = biochemkftform2(request.POST,instance=pat)
        bio3 = biochemlftform3(request.POST,instance=pat)
        bio4 = biochemlftoptionform4(request.POST,instance=pat)
        bio5 = biochemlftoptionform5(request.POST,instance=pat)

        if b.is_valid() or c.is_valid() or u.is_valid() or ur.is_valid() or st.is_valid() or semen.is_valid() or f1.is_valid() or f2.is_valid() or f3.is_valid()\
                or f4.is_valid() or f5.is_valid() or f6.is_valid() or ser1.is_valid() or ser2.is_valid() or ser3.is_valid() or ser4.is_valid() or ser5.is_valid() \
                or ser6.is_valid() or ser7.is_valid() or res.is_valid() or dan1.is_valid or dan6.is_valid() or dan2.is_validor or dan3.is_valid or dan4.is_valid or dan5.is_valid or \
                alkal.is_valid() or bio1.is_valid() or bio2.is_valid() or bio3.is_valid() or bio4.is_valid() or bio5.is_valid():
            b.save()
            c.save()
            u.save()
            ur.save()
            st.save()
            semen.save()
            f1.save()
            f2.save()
            dan1.save()
            dan2.save()
            dan3.save()
            dan4.save()
            dan5.save()
            dan6.save()
            f3.save()
            f4.save()
            f5.save()
            f6.save()
            ser1.save()
            ser2.save()
            ser3.save()
            ser4.save()
            ser5.save()
            ser6.save()
            ser7.save()
            bio1.save()
            bio2.save()
            bio3.save()
            bio4.save()
            bio5.save()
            res.save()
            alkal.save()
            return redirect('/app/home/')
    params = {
        'form': pat,
        'b': b,    "b1":b1,"b2":b2,"b3":b3,"b4":b4,
        'c':c    ,   "cbc":Cbc,
        'u':u    ,   "U1":U1,"U2":U2,
        'ur':ur    ,   'Ur':Ur,
        'st':st    ,   'St':St,
        'semen':semen    ,   'sem':sem,
        'f1':f1, "f2": f2, "f3":f3, "f4":f4, "f5":f5,"f6":f6,'alkal':alkal,              'F1':F1,'F2':F2,'F3':F3,'F4':F4,'F5':F5,'F6':F6,
        "ser1":ser1,"ser2":ser2,"ser3":ser3,"ser4":ser4,"ser5":ser5,"ser6":ser6,"ser7":ser7,                  "sero1":sero1,"sero2":sero2,"sero3":sero3,"sero4":sero4,"sero5":sero5,"sero6":sero6,"sero7":sero7,
        'bio1':bio1,'bio2':bio2,'bio3':bio3,'bio4':bio4,'bio5':bio5,'res':res,'alk':alk,           'B1':B1,'B2':B2,'B3':B3,'B4':B4,'B5':B5,
        'dan1':dan1,"dan2":dan2,'dan3':dan3,'dan4':dan4,'dan5':dan5,'dan6':dan6,                       'd1':d1,'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6':d6,
    }
    return render(request, 'tests/basic.html', params)


def result(request,pk):
    pat = Patient.objects.get(id=pk)
    b1 = pat.t1
    b2 = pat.t2
    b3 = pat.t3
    b4 = pat.t4
    Cbc = pat.cbc
    U1 = pat.u1
    U2 = pat.u2
    Ur=pat.ur
    St=pat.st
    sero1=pat.St1
    sero2=pat.St2
    sero3=pat.St3
    alk=pat.AkPh
    sero4=pat.St4
    sero5=pat.St5
    sero6=pat.St6
    sero7=pat.St7
    d1 = pat.serumcrea
    d2 = pat.Uric_Acid
    d3 = pat.Serum_Calcium
    d4 = pat.Serum_Sodium
    d5 = pat.Serum_Pottasium
    d6 = pat.Sgot
    sem=pat.semen
    F1 = pat.haemoglobin
    F2 = pat.bloodgrp
    F3 = pat.BT_CT
    F4 = pat.TotalCount
    F5 = pat.DiffCount
    F6 = pat.usr
    B1 = pat.blipid
    B2 = pat.KFT
    B3 = pat.leftest
    B4 = pat.Sgpt
    B5=pat.bilirubin
    ldl=2
    vldl=0
    rat=6
    agratio=8
    result=0
    glob=0
    if B1:
        ldl1=(pat.Total_chol)
        ldl2=(pat.HDL)
        print(type(ldl1))

        ldl=ldl1-ldl2
        vldl1=pat.Serum
        rat1=ldl1/ldl2
        rat = "{0:.2f}".format(rat1)
        vldlf=vldl1-ldl
        vldl="{0:.2f}".format(vldlf)
    if B3:
        glob=(pat.Tpro)-(pat.Talbo)
        ag=(pat.Talbo)/glob
        agratio="{0:.2f}".format(ag)
    if B5:
        res=(pat.totka)-(pat.directa)
        result="{0:.2f}".format(res)
    param={'form':pat,"b1":b1,"b2":b2,"b3":b3,"b4":b4, "cbc":Cbc,'U1':U1,'U2':U2,
           'Ur':Ur,'St':St,'sem':sem,'F1':F1,'F2':F2,'F3':F3,'F4':F4,'F5':F5,'F6':F6
           , 'sero1':sero1,'sero2':sero2,'sero3':sero3,'sero4':sero4,'sero5':sero5,
           'sero6':sero6,'sero7':sero7,'B1':B1,'B2':B2,'B3':B3,'B4':B4,
           'B5':B5,'ldl':ldl,'vldl':vldl,'rat':rat,'agratio':agratio,'result':result,
           'glob':glob,'alk':alk,'d1':d1,'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6':d6}
    return render(request,'tests/result.html',param)


def about(request):
    mapboxgl_access_Token = 'pk.eyJ1IjoibWFzaGhvb2RkYW5pc2giLCJhIjoiY2s5czY2OXNjMTE0OTNocG54aThxNnZvNiJ9.0M_ZREIkSlqGiiGdavw9KQ';
    context={'mapboxgl_access_Token':mapboxgl_access_Token}
    return render(request,'tests/about.html',context)