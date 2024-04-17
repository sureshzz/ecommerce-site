from django import forms
from .models import Account



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
    }))
    confirm_password = forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder': 'confirm password',
    }))
    class Meta:
        model = Account
        fields = ['first_name','last_name','password','email','phone_number']
    
    def clean(self):
        cleaned_data = super(RegistrationForm ,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            # raise forms.ValidationError("password doesnot match!")
            print("errorrrrrrrrrrrrr")
            raise forms.ValidationError("password doesnot match!")
        
    
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email '
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone number '
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
                