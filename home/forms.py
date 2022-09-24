from django import forms
from home.models import *

class uform_dr(forms.ModelForm):
    class Meta:
        model = doctor
        fields ="__all__"

class uform_pt(forms.ModelForm):
    class Meta:
        model = patient
        fields ="__all__"
    

class uform_ad(forms.ModelForm):
    class Meta:
        model = admin
        fields ="__all__"