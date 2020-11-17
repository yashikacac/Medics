from django import forms
from django.forms import ModelForm
from .models import Input,Hospital

class InputForm(forms.ModelForm):
	
	class Meta:
		model = Input
		fields = ('location',)

class HospitalForm(forms.ModelForm):

	class Meta:
		model = Hospital
		fields = ('Name','Address','Locality','City','State','Oxygen_Cylinder','Beds','MRI_Machine',)