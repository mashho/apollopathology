from django.db import models


# Create your models here.


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, default="")
    RecievedDate = models.DateField()
    Age = models.IntegerField(default=0)
    choice = {
        ('Male', 'Male'),
        ('Female', 'Female')
    }
    Sex = models.CharField(max_length=10, choices=choice)
    ReportDate = models.DateField()
    ReferenceBy = models.CharField(max_length=100, null=True)

    #Blood checkup
    t1=models.BooleanField('Blodd Sugar(F)', default=False, blank=True)
    t1form = models.CharField(max_length=20, blank=True)
    t2=models.BooleanField('Blodd Sugar(PP)', default=False, blank=True)
    t2form = models.CharField(max_length=20, blank=True)
    t3=models.BooleanField('2hr after Food/med', default=False, blank=True)
    t3form = models.CharField(max_length=20, blank=True)
    t4=models.BooleanField('Blodd Sugar(R)', default=False, blank=True)
    t4form = models.CharField(max_length=20, blank=True)

    # CBC new
    cbc = models.BooleanField('CBC test', default=False, blank=True)
    Haemoglobin1 = models.CharField(max_length=20, blank=True)
    PCV = models.CharField(max_length=20, blank=True)
    MCV = models.CharField(max_length=20, blank=True)
    MCH = models.CharField(max_length=20, blank=True)
    MCHC = models.CharField(max_length=20, blank=True)
    Total_RBC = models.CharField(max_length=20, blank=True)
    Total_WBC = models.CharField(max_length=20, blank=True)
    Platelet = models.CharField(max_length=20, blank=True)
    Neutrophils = models.CharField(max_length=20, blank=True)
    Lymphocytes = models.CharField(max_length=20, blank=True)
    Eosonophils = models.CharField(max_length=20, blank=True)
    Monocytes = models.CharField(max_length=20, blank=True)
    Basophils = models.CharField(max_length=20, blank=True)
    ESR = models.CharField(max_length=20, blank=True)



    #urine culture and sensitivity
    u1 = models.BooleanField('No Organism', default=False, blank=True)
    u2 = models.BooleanField('With organism', default=False, blank=True)
    organism = models.CharField(max_length=20, blank=True)
    ce = models.CharField(max_length=20, blank=True)
    ga = models.CharField(max_length=20, blank=True)
    az = models.CharField(max_length=20, blank=True)
    ge = models.CharField(max_length=20, blank=True)
    lo = models.CharField(max_length=20, blank=True)
    am = models.CharField(max_length=20, blank=True)
    co = models.CharField(max_length=20, blank=True)
    chlo = models.CharField(max_length=20, blank=True)
    no = models.CharField(max_length=20, blank=True)
    cep = models.CharField(max_length=20, blank=True)
    ery = models.CharField(max_length=20, blank=True)
    cipro = models.CharField(max_length=20, blank=True)
    of = models.CharField(max_length=20, blank=True)
    cefo = models.CharField(max_length=20, blank=True)
    pen = models.CharField(max_length=20, blank=True)
    amo = models.CharField(max_length=20, blank=True)
    pf = models.CharField(max_length=20, blank=True)
    lev = models.CharField(max_length=20, blank=True)
    lin = models.CharField(max_length=20, blank=True)
    cef = models.CharField(max_length=20, blank=True)
    spar = models.CharField(max_length=20, blank=True)
    nal = models.CharField(max_length=20, blank=True)
    amox = models.CharField(max_length=20, blank=True)

    #urine routine
    ur = models.BooleanField('Urine Routine Examination', default=False, blank=True)
    col = models.CharField(max_length=20, blank=True)
    app = models.CharField(max_length=20, blank=True)
    dep = models.CharField(max_length=20, blank=True)
    spg = models.CharField(max_length=20, blank=True)
    ph = models.CharField(max_length=20, blank=True)
    reac = models.CharField(max_length=20, blank=True)
    su = models.CharField(max_length=20, blank=True)
    alb = models.CharField(max_length=20, blank=True)
    pho = models.CharField(max_length=20, blank=True)
    ura = models.CharField(max_length=20, blank=True)
    bils = models.CharField(max_length=20, blank=True)
    bilp = models.CharField(max_length=20, blank=True)
    uro = models.CharField(max_length=20, blank=True)
    ket = models.CharField(max_length=20, blank=True)
    ben = models.CharField(max_length=20, blank=True)
    chy = models.CharField(max_length=20, blank=True)
    leu = models.CharField(max_length=20, blank=True)
    eryt = models.CharField(max_length=20, blank=True)
    epi = models.CharField(max_length=20, blank=True)
    gra = models.CharField(max_length=20, blank=True)
    hy = models.CharField(max_length=20, blank=True)
    cal = models.CharField(max_length=20, blank=True)
    trip = models.CharField(max_length=20, blank=True)
    amor = models.CharField(max_length=20, blank=True)
    oth = models.CharField(max_length=20, blank=True)



    #stool
    st= models.BooleanField('Stool Routine Examination', default=False, blank=True)
    clr=models.CharField(max_length=20, blank=True)
    con=models.CharField(max_length=20, blank=True)
    odo=models.CharField(max_length=20, blank=True)
    mus=models.CharField(max_length=20, blank=True)
    react=models.CharField(max_length=20, blank=True)
    red=models.CharField(max_length=20, blank=True)
    occ=models.CharField(max_length=20, blank=True)
    EH=models.CharField(max_length=20, blank=True)
    en=models.CharField(max_length=20, blank=True)
    gia=models.CharField(max_length=20, blank=True)
    Rou=models.CharField(max_length=20, blank=True)
    hoo=models.CharField(max_length=20, blank=True)
    pin=models.CharField(max_length=20, blank=True)
    whip=models.CharField(max_length=20, blank=True)
    tap=models.CharField(max_length=20, blank=True)
    na=models.CharField(max_length=20, blank=True)
    lar=models.CharField(max_length=20, blank=True)
    deg=models.CharField(max_length=20, blank=True)
    comp=models.CharField(max_length=20, blank=True)
    undi=models.CharField(max_length=20, blank=True)
    anyo=models.CharField(max_length=20, blank=True)
    other=models.CharField(max_length=20, blank=True)


    #semen
    semen= models.BooleanField('Semen Routine Examination', default=False, blank=True)


    MOC=models.CharField(max_length=20, blank=True)
    Ab=models.CharField(max_length=20, blank=True)
    Amount=models.CharField(max_length=20, blank=True)
    CL=models.CharField(max_length=20, blank=True)
    Re=models.CharField(max_length=20, blank=True)
    TC=models.CharField(max_length=20, blank=True)
    MO=models.CharField(max_length=20, blank=True)
    half=models.CharField(max_length=20, blank=True)
    one=models.CharField(max_length=20, blank=True)
    two=models.CharField(max_length=20, blank=True)
    nor=models.CharField(max_length=20, blank=True)
    abnor=models.CharField(max_length=20, blank=True)
    pc=models.CharField(max_length=20, blank=True)
    epith=models.CharField(max_length=20, blank=True)

    #Haematology

    haemoglobin = models.BooleanField('Haemoglobin', default=False, blank=True)
    f1 = models.CharField(max_length=20, blank=True)
    bloodgrp = models.BooleanField('Blood Group', default=False, blank=True)
    f2 = models.CharField(max_length=20, blank=True)
    f3 = models.CharField(max_length=20, blank=True)
    BT_CT = models.BooleanField('BT-CT', default=False, blank=True)
    f4 = models.CharField(max_length=20, blank=True)
    f5 = models.CharField(max_length=20, blank=True)
    TotalCount = models.BooleanField('TC(Total Count)', default=False, blank=True)
    f6 = models.CharField(max_length=20, blank=True)
    DiffCount = models.BooleanField('DC(Differential Count)', default=False, blank=True)
    f7 = models.CharField(max_length=20, blank=True)
    f8 = models.CharField(max_length=20, blank=True)
    f9 = models.CharField(max_length=20, blank=True)
    f10 = models.CharField(max_length=20, blank=True)
    f11 = models.CharField(max_length=20, blank=True)
    usr = models.BooleanField('ESR', default=False, blank=True)
    f12 = models.CharField(max_length=20, blank=True)


    #Serology
    St1 = models.BooleanField('HIV+HBsAG+VDRL', default=False, blank=True)
    s1 = models.CharField(max_length=20, blank=True)
    s2 = models.CharField(max_length=20, blank=True)
    s3 = models.CharField(max_length=20, blank=True)
    St2 = models.BooleanField('Dengue Test', default=False, blank=True)
    s4 = models.CharField(max_length=20, blank=True)
    s5 = models.CharField(max_length=20, blank=True)
    s6 = models.CharField(max_length=20, blank=True)
    St3 = models.BooleanField('ELISA for TYPHOID & HCV', default=False, blank=True)
    s7 = models.CharField(max_length=20, blank=True)
    s8 = models.CharField(max_length=20, blank=True)
    s9 = models.CharField(max_length=20, blank=True)
    St4 = models.BooleanField('Rapid+Optimal Test Maleria', default=False, blank=True)
    s10 = models.CharField(max_length=20, blank=True)
    s11 = models.CharField(max_length=20, blank=True)
    St5 = models.BooleanField('Widal Test', default=False, blank=True)
    St9 = models.CharField(max_length=20, blank=True)
    s12 = models.CharField(max_length=20, blank=True)
    s13 = models.CharField(max_length=20, blank=True)
    s14 = models.CharField(max_length=20, blank=True)
    s15 = models.CharField(max_length=20, blank=True)
    s16 = models.CharField(max_length=20, blank=True)
    s17 = models.CharField(max_length=20, blank=True)
    s18 = models.CharField(max_length=20, blank=True)
    s19 = models.CharField(max_length=20, blank=True)
    s20 = models.CharField(max_length=20, blank=True)
    s21 = models.CharField(max_length=20, blank=True)
    s22 = models.CharField(max_length=20, blank=True)
    s23 = models.CharField(max_length=20, blank=True)
    s24 = models.CharField(max_length=20, blank=True)
    s25 = models.CharField(max_length=20, blank=True)
    s26 = models.CharField(max_length=20, blank=True)
    s27 = models.CharField(max_length=20, blank=True)
    s28 = models.CharField(max_length=20, blank=True)
    s29 = models.CharField(max_length=20, blank=True)
    s30 = models.CharField(max_length=20, blank=True)
    s31 = models.CharField(max_length=20, blank=True)
    s32 = models.CharField(max_length=20, blank=True)
    s33 = models.CharField(max_length=20, blank=True)
    s34 = models.CharField(max_length=20, blank=True)
    s35 = models.CharField(max_length=20, blank=True)
    St6 = models.BooleanField('Mantoux+Sputium Test', default=False, blank=True)
    s36 = models.CharField(max_length=20, blank=True)
    s37 = models.CharField(max_length=20, blank=True)
    s38 = models.CharField(max_length=20, blank=True)
    St7 = models.BooleanField('Rapid Test', default=False, blank=True)
    s39 = models.CharField(max_length=20, blank=True)
    s40 = models.CharField(max_length=20, blank=True)
    s41 = models.CharField(max_length=20, blank=True)




    #biochemistry LIPID

    Total_chol=models.FloatField(null=True,blank=True)
    Serum=models.FloatField( blank=True,null=True)
    HDL=models.FloatField( blank=True,null=True)
    blipid = models.BooleanField('Biochemistry-LIPID', default=False, blank=True)

    # biochemistry KFT
    KFT = models.BooleanField('Blood Urea', default=False, blank=True)
    BU = models.CharField(max_length=20, blank=True)
    serumcrea = models.BooleanField('Serum Creatinine', default=False, blank=True)
    Screa = models.CharField(max_length=20, blank=True)
    Uric_Acid = models.BooleanField('Serum Uric Acid', default=False, blank=True)
    SMale = models.CharField(max_length=20, blank=True)
    SFeMale = models.CharField(max_length=20, blank=True)
    Serum_Calcium= models.BooleanField('Serum Calcium', default=False, blank=True)
    SCalcium = models.CharField(max_length=20, blank=True)
    Serum_Sodium = models.BooleanField('Serum Sodium', default=False, blank=True)
    SSodium = models.CharField(max_length=20, blank=True)
    Serum_Pottasium= models.BooleanField('Serum Pottasium', default=False, blank=True)
    SPott = models.CharField(max_length=20, blank=True)


    #bio-LFT
    Sgpt = models.BooleanField('S.G.P.T ', default=False, blank=True)
    sgptalt = models.CharField(max_length=20, blank=True)
    Sgot=models.BooleanField('S.G.O.T ', default=False, blank=True)
    sgotfield = models.CharField(max_length=20, blank=True)

    leftest = models.BooleanField('Serum Protien', default=False, blank=True)
    Tpro =  models.FloatField(max_length=20, blank=True,null=True)
    Talbo = models.FloatField(max_length=20, blank=True,null=True)

    bilirubin = models.BooleanField('Serum Bilirubin', default=False, blank=True)
    totka = models.FloatField(max_length=5, blank=True,null=True)
    directa = models.FloatField(max_length=5, blank=True,null=True)
    AkPh = models.BooleanField('Alkaline Phosphate',default=False,blank=True)
    akg = models.CharField(max_length=20, blank=True)
    result=models.CharField(max_length=20, blank=True)





    def __str__(self):
        return self.Name




