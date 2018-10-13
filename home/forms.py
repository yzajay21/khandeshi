from django import forms
from .models import RegisterProfile


class RegisterProfileForm(forms.ModelForm):
	class Meta:
		model = RegisterProfile
		fields = '__all__'
		widgets = {
        'date_of_birth': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }	
		#fields 	= ['first_name','middle_name',
				 # 'last_name','mobile_no',
				 # 'description','date_of_birth'
				 # ,'pan','aadhar',
				 # 'city','address',
				#  'permanent_address','name_of_individual',
				#  'mobile_no_of_friend','va_type',
				#]









	