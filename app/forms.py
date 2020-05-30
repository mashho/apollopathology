from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta():
        model = Patient
        fields = '__all__'


class bloodform(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['t1form','t2form','t3form','t4form']

class CBCForm(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['Haemoglobin1', 'PCV', 'MCV', 'MCH', 'MCHC', 'Total_RBC', 'Total_WBC', 'Platelet', 'Neutrophils', 'Lymphocytes', 'Eosonophils', 'Monocytes', 'Basophils', 'ESR']



class urineform(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  [ 'organism', 'ce', 'ga', 'az', 'ge', 'lo', 'am', 'co', 'chlo', 'no', 'cep', 'ery', 'cipro', 'of', 'cefo', 'pen', 'amo', 'pf', 'lev', 'lin', 'cef', 'spar', 'nal', 'amox']



class urineroutineform(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  [ 'col','app','dep','spg','ph','reac','su','alb','pho','ura','bils','bilp', 'uro','ket','ben','chy','leu','eryt','epi','gra','hy','cal','trip','amor','oth']

class Stoolform(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  [ 'clr','con','odo','mus','react','red','occ','EH','en','gia','Rou','hoo', 'pin','whip','tap','na','lar','deg','comp','undi','anyo','other']



class semenform(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['MOC', 'Ab', 'Amount', 'CL', 'Re', 'TC', 'MO', 'half', 'one', 'two', 'nor', 'abnor', 'pc', 'epi']



class HaematologyForm1(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['f1']


class HaematologyForm2(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['f2','f3']

class HaematologyForm3(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['f4','f5']

class HaematologyForm4(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['f6']


class HaematologyForm5(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['f7','f8', 'f9', 'f10', 'f11']

class HaematologyForm6(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['f12']

class serologyform1(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['s1','s2','s3',]
class serologyform2(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['s4','s5','s6',]
class serologyform3(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['s7','s8','s9',]
class serologyform4(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['s10','s11']
class serologyform5(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['s12','St9','s13','s14','s15','s16','s17','s18','s19','s20','s21','s22','s23','s24','s25','s26','s27','s28','s29','s30','s31','s32','s33','s34','s35',]
class serologyform6(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['s36','s37','s38',]
class serologyform7(forms.ModelForm):
    class Meta():
        model = Patient
        fields =  ['s39','s40','s41',]

class biochemlipidform1(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['Total_chol', 'Serum', 'HDL', ]

class biochemkftform2(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['BU']

class biochemlftform3(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['Tpro','Talbo', ]

class biochemlftoptionform4(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['sgptalt' ]


class biochemlftoptionform5(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['totka', 'directa' ]

class resultform(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['result']


class dannu1(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['Screa']


class dannu2(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['SMale','SFeMale']


class dannu3(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['SCalcium']


class dannu4(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['SSodium']


class dannu5(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['SPott']



class alkali(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['akg',]


class dannu6(forms.ModelForm):
    class Meta():
        model = Patient
        fields = ['sgotfield',]

