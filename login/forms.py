from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import user_acc

class user_accForm(forms.ModelForm):
    
    class Meta:
        model = user_acc
        
        fields = ('fName','lName','usr_contact_num','usr_gender','usr_city','usr_barangay','usr_street','usr_email','usr_zipcode','usr_province','usr_username','usr_password')

        widgets = {
            #basic info that is needed
            'fName' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
            'lName' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
            'usr_contact_num' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
            'usr_gender' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
            'usr_city' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
            'usr_barangay' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
            'usr_street' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
            'usr_email' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
            'usr_zipcode' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
            'usr_province' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
        
            #Account configs
            'usr_username' : forms.TextInput(attrs={'class':"form-control form-control-lg"}),
            'usr_password' : forms.PasswordInput(attrs={'class':"form-control form-control-lg"}),
           
        }


        """
        #basic info that is needed
        fName = forms.TextInput(label='First Name',max_length=250)
        lName = forms.TextInput(label='Last Name',max_length=250)
        usr_contact_num = forms.TextInput(label='Contact No.')
        usr_gender = forms.TextInput(label='Gender',max_length=250)
        usr_city = forms.TextInput(label='City',max_length=250)
        usr_barangay = forms.TextInput(label='Barangay',max_length=250)
        usr_street = forms.TextInput(label='Street',max_length=250)
        usr_email = forms.TextInput(label='Email',max_length=250)
        usr_zipcode = forms.TextInput(label='Zip Code',max_length=150)
        usr_province = forms.TextInput(label='Province',max_length=250)
        
        

        #Account configs
        usr_username = forms.TextInput(label='Username',max_length=250)
        usr_password = forms.TextInput(label='Password',max_length=250)
        usr_email = forms.TextInput(label='Email',max_length=250)
        
    
        
        """
        